
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from datetime import datetime, date, time
from .forms import UserRegistrationForm, CustomLoginForm, BookingForm
from .models import Table, Booking
from .utils import find_available_table
import time as time_control
from django.contrib import messages


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
            messages.success(
                request, 'Registration successful! Welcome to East flavore')
            return redirect('/')
        else:
            messages.error(
                request, 'Registration failed. Please check the form again.')
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
                messages.success(request, f"Welcome back, {username}!")
                return redirect('book-table')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'booking/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('home')


# BOOKING
@login_required
def book_table(request):
    """
    Handles table booking for logged-in users.
    On POST, processes the booking form, finds an available table,
    and creates a booking or shows an error if no table is available.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print(form.data)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            guests = form.cleaned_data['guests']

            tzname = request.COOKIES.get("django_timezone", "UTC")

            # Check if the selected date/time is in the past
            current_datetime = datetime.now()
            selected_datetime = datetime.combine(date, time)

            if selected_datetime < current_datetime:
                messages.error(
                    request,
                    "Booking time must be at least"
                    "-one minute ahead of the current time!")
                return render(
                    request, 'booking/book_table.html', {'form': form})

            # Find available table for the given date, time, guests
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
                messages.success(
                    request, 'Your booking is successful!')
                return redirect(reverse('user-bookings'))
            else:
                # No available table found, show an error message
                form.add_error(
                    None,
                    (
                        "Sorry, no table available for the selected date,"
                        "time, and guests, or you have booked table already in this hour!"
                        ))

    else:
        form = BookingForm()
    return render(request, 'booking/book_table.html', {'form': form})


@login_required
def user_bookings(request):
    """
    Retrieves all bookings made by the logged-in user and
    renders them in a template.
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
        messages.error(request, 'Booking canceled successfully')
        return JsonResponse(response_data, status=200)
    else:
        messages.error(request, 'Booking not found')
        return JsonResponse(
            {
                'error': "Booking not found"
                "or you don't have permission to cancel it."
                       },
            status=404)


@login_required
def get_booking(request, id):
    """
    get specific booking
    """
    booking = get_object_or_404(Booking, id=id)
    return render(
        request,
        'booking/edit_book.html',
        {'booking': booking, 'get_range': range(1, 11)}
        )


@login_required
def update_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.user != booking.user:
        messages.error(request, 'Invalid user!')
        return redirect(reverse('login'))

    if request.method == 'POST':
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guests = request.POST.get('guests')
        _date = datetime.strptime(date_str, "%Y-%m-%d").date()
        _time = datetime.strptime(time_str, "%H:%M").time()
        _guests = int(guests)

        current_time_str = time_control.strftime(
            "%H:%M", time_control.localtime())
        current_time = datetime.strptime(current_time_str, "%H:%M").time()

        if _date and _time and _date == date.today() and _time > current_time :
            booking.date = _date
            booking.time = _time
            
        if _date and _time and _date == date.today() and _time <= current_time :
            messages.error(request, 'Invalid time!')
            return render(
                request,
                'booking/edit_book.html', {
                    'booking':booking, 'get_range':range(1,11)})
        else:
            if _date and _date >= date.today():
                booking.date = _date
            else:
                messages.error(request, 'Invalid date!')
                return render(
                    request,
                    'booking/edit_book.html',
                    {'booking': booking, 'get_range': range(1, 11)})

            if _time and (time(11, 0) <= _time < time(22, 0)):
                booking.time = _time
            else:
                messages.error(request, 'Invalid time!')
                return render(
                    request,
                    'booking/edit_book.html',
                    {'booking': booking, 'get_range': range(1, 11)})

            if _guests and 11 > _guests > 0:
                booking.guests = _guests
            else:
                messages.error(request, 'book for guests from 1 to 10!')
                return render(
                    request,
                    'booking/edit_book.html',
                    {'booking': booking, 'get_range': range(1, 11)})
        booking.save()
        messages.success(request, 'Booking updated successfully!')
    return redirect(reverse('user-bookings'))
