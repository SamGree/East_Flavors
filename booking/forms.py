from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Booking

import datetime


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class BookingForm(forms.ModelForm):
    today = datetime.date.today()
    opening_time = datetime.time(11, 0)
    closing_time = datetime.time(9, 0)
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': today}),
        label='Booking Date'
    )
    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'type': 'time', 'min': opening_time, 'max': closing_time}),
        label='Booking Time'
    )

    class Meta:
        model = Booking
        fields = ['date', 'time', 'guests']

    def clean_date(self):
        # additional layer of security, can't select if date is in past
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Booking date cannot be in the past.")
        return date

    def clean_time(self):
        # defining when restaurant is open
        time = self.cleaned_data['time']
        opening_time = datetime.time(11, 0)
        closing_time = datetime.time(22, 0)
        if not (opening_time <= time <= closing_time):
            raise forms.ValidationError(
                "Booking time must be within (11:00 AM - 11:00 PM).")
        return time