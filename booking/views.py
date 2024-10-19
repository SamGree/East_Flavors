from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse

from .forms import UserRegistrationForm, CustomLoginForm, BookingForm
from .models import Table, Booking
from .utils import find_available_table
import zoneinfo
from django.utils import timezone


def register(request):
    """
    Handles user registration. If the request method is POST, it processes 
    the form and registers the user if valid. Upon successful registration, 
    logs the user in and redirects to the 'book-table' page.
    Renders the registration form if the request method is GET.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-table')
    else:
        form = UserRegistrationForm()
    return render(request, 'booking/register.html', {'form': form})


def user_login(request):
    """
    Handles user login. Processes the login form if the request method is POST, 
    authenticates the user, and logs them in if credentials are valid. 
    Redirects to the 'book-table' page upon successful login.
    Renders the login form if the request method is GET.
    """
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('book-table')
    else:
        form = CustomLoginForm()
    return render(request, 'booking/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


# BOOKING
@login_required
def book_table(request):
    """
    Handles table booking for logged-in users.
    - On POST, processes the booking form, finds an available table, 
      and creates a booking or shows an error if no table is available.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print(form.data)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            guests = form.cleaned_data['guests']

            tzname = request.COOKIES.get("django_timezone")

            # Find an available table for the given date, time, and number of guests
            table = find_available_table(
                date, time, guests, request.user, tzname)

            if table:
                # Create the booking if an available table is found
                booking = Booking.objects.create(
                    user=request.user,
                    table=table,
                    date=date,
                    time=time,
                    guests=guests
                )
                return redirect(reverse('user-bookings'))
            else:
                # No available table found, show an error message
                form.add_error(
                    None, "No available table for the selected date, time, and number of guests.")

    else:
        form = BookingForm()
    return render(request, 'booking/book_table.html', {'form': form})


@login_required
def user_bookings(request):
    """
    Retrieves all bookings made by the logged-in user and renders them in a template.
    """
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'booking/bookings.html', context)


@login_required
def cancel_booking(request, id):
    """
    Cancels a booking for the logged-in user based on the booking ID.
     Returns a success message if the booking is found and canceled.
     Returns an error if the booking is not found or the user has no permission.
    """
    booking = Booking.objects.filter(user=request.user, id=id)
    if booking.exists():
        booking.delete()
        response_data = {'message': "Booking canceled successfully!"}
        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({'error': "Booking not found or you don't have permission to cancel it."}, status=404)
