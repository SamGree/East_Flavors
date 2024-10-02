from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from django.utils import timezone

@login_required
def make_reservation(request):
    if request.method == "POST":
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        
        Reservation.objects.create(
            user=request.user,
            date=date,
            time=time,
            number_of_guests=guests
        )
        return redirect('reservation_success')
    return render(request, 'booking/make_reservation.html')

# Create your views here.
