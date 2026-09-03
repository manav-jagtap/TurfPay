from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from turfs.models import Slot, Turf
from .models import Booking


class BookingTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testcustomer",
            password="Test@12345",
        )

        self.owner = User.objects.create_user(
            username="testowner",
            password="Owner@12345",
        )

        self.turf = Turf.objects.create(
            owner=self.owner,
            name="Test Turf",
            location="Latur",
            sport_type="cricket",
            price_per_hour=800,
        )

        self.slot = Slot.objects.create(
            turf=self.turf,
            date=timezone.localdate() + timedelta(days=1),
            start_time="18:00",
            end_time="19:00",
        )

        self.client.login(
            username="testcustomer",
            password="Test@12345",
        )

    def test_customer_can_book_slot(self):
        response = self.client.post(
            reverse(
                "book_slot",
                args=[self.slot.id],
            )
        )

        self.assertRedirects(
            response,
            reverse("my_bookings"),
        )

        self.assertTrue(
            Booking.objects.filter(
                user=self.user,
                slot=self.slot,
                status="confirmed",
            ).exists()
        )

        self.slot.refresh_from_db()

        self.assertFalse(
            self.slot.is_available
        )

    def test_customer_can_cancel_booking(self):
        booking = Booking.objects.create(
            user=self.user,
            slot=self.slot,
        )

        self.slot.is_available = False
        self.slot.save()

        response = self.client.post(
            reverse(
                "cancel_booking",
                args=[booking.id],
            )
        )

        self.assertRedirects(
            response,
            reverse("my_bookings"),
        )

        booking.refresh_from_db()
        self.slot.refresh_from_db()

        self.assertEqual(
            booking.status,
            "cancelled",
        )

        self.assertTrue(
            self.slot.is_available
        )

    def test_booking_page_requires_login(self):
        self.client.logout()

        response = self.client.get(
            reverse("my_bookings")
        )

        self.assertEqual(
            response.status_code,
            302,
        )