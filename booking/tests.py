from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Table, Booking
from datetime import datetime, timedelta


class BookingTests(TestCase):
    def setUp(self):
        """
        Create test users and a table.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='testpass123')
        self.user2 = User.objects.create_user(
            username='user2', password='testpass123')
        self.table = Table.objects.create(capacity=4)

        """
        User2 makes a booking
        """
        self.booking = Booking.objects.create(
            user=self.user2,
            table=self.table,
            date=datetime.today().date() + timedelta(days=1),
            time=datetime.now().time(),
            guests=2
        )

    def test_user1_cannot_update_user2_booking(self):
        """
        Ensure that User1 cannot update User2's booking.
        """
        self.client.login(username='user1', password='testpass123')

        response = self.client.post(
            reverse('update-booking', args=[self.booking.id]), {
             'date': (datetime.today().date() + timedelta(
                 days=2)).strftime('%Y-%m-%d'),
             'time': '14:00',
             'guests': 3})

        self.booking.refresh_from_db()
        """
        Booking should remain unchanged
        """
        self.assertNotEqual(
            self.booking.date, datetime.today().date() + timedelta(days=2))
        self.assertEqual(response.status_code, 302)

    def test_user1_cannot_cancel_user2_booking(self):
        """
        Ensure that User1 cannot cancel User2's booking.
        """
        self.client.login(username='user1', password='testpass123')

        response = self.client.post(
            reverse('cancel-booking', args=[self.booking.id]))

        self.assertEqual(response.status_code, 404)
        self.assertTrue(Booking.objects.filter(id=self.booking.id).exists())

    def test_user1_cannot_book_for_user2(self):
        """
        Ensure that a booking is always assigned to the logged-in user.
        """
        self.client.login(username='user1', password='testpass123')

        response = self.client.post(reverse('book-table'), {
            'date': (datetime.today().date() + timedelta(
                 days=3)).strftime('%Y-%m-%d'),
            'time': '15:00',
            'guests': 2
        })

        # Check if a booking was created
        new_booking = Booking.objects.filter(user=self.user1).first()
        self.assertIsNotNone(new_booking)  # Should exist
        self.assertEqual(new_booking.user, self.user1)
        self.assertNotEqual(new_booking.user, self.user2)

        self.assertEqual(response.status_code, 302)
        