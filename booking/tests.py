from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Table, Booking
from datetime import date, time
from django.utils import timezone


class BookingTests(TestCase):
    def setUp(self):
        # Create a user and log them in for testing
        self.user = User.objects.create_user(
            username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        # Set a default timezone for the session
        self.client.cookies['django_timezone'] = 'UTC'
        # Create a table for testing
        self.table = Table.objects.create(capacity=4)


class AuthTests(TestCase):
    def test_register_user(self):
        """
        Test user registration.
        """
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 302)
        # Should redirect after registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_user(self):
        """
        Test user login.
        """
        user = User.objects.create_user(
            username='testuser', password='password')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)
        # Should redirect after login
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_logout_user(self):
        """
        Test user logout.
        """
        user = User.objects.create_user(
            username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        # Should redirect after logout
        self.assertNotIn('_auth_user_id', self.client.session)


class BookingTests(TestCase):
    def setUp(self):
        # Create a user and log them in for testing
        self.user = User.objects.create_user(
            username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        # Create a table for testing
        self.table = Table.objects.create(capacity=4)

    def test_book_table(self):
        """
        Test booking a table with valid data.
        """
        booking_date = date.today()
        booking_time = time(21, 0)  # 9:00 PM
        response = self.client.post(reverse('book-table'), {
            'date': booking_date,
            'time': booking_time,
            'guests': 2
        })
        self.assertEqual(response.status_code, 302)
        # Should redirect upon successful booking
        self.assertTrue(
            Booking.objects.filter(
                user=self.user,
                table=self.table,
                date=booking_date,
                time=booking_time).exists())

    def test_user_bookings_view(self):
        """
        Test viewing user bookings.
        """
        Booking.objects.create(
            user=self.user,
            table=self.table,
            date=date.today(), time=time(18, 0), guests=2)
        response = self.client.get(reverse('user-bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Booking for")

    def test_cancel_booking(self):
        """
        Test canceling a booking.
        """
        booking = Booking.objects.create(
            user=self.user,
            table=self.table, date=date.today(), time=time(18, 0), guests=2)
        response = self.client.post(reverse('cancel-booking',
                                    args=[booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Booking.objects.filter(id=booking.id).exists())

    def test_cancel_booking_unauthorized(self):
        """
        Test that a user cannot cancel another user's booking.
        """
        other_user = User.objects.create_user(
            username='otheruser', password='password')
        other_booking = Booking.objects.create(
            user=other_user,
            table=self.table,
            date=date.today(), time=time(18, 0), guests=2)

        response = self.client.post(
            reverse('cancel-booking', args=[other_booking.id]))
        self.assertEqual(response.status_code, 404)
        # Should return 404 as the booking doesn't belong to the logged-in user