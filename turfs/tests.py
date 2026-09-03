from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Slot, Turf


class TurfOwnerTests(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user(
            username="testowner",
            password="Owner@12345",
        )

        self.customer = User.objects.create_user(
            username="testcustomer",
            password="Customer@12345",
        )

        self.other_owner = User.objects.create_user(
            username="otherowner",
            password="Other@12345",
        )

        self.turf = Turf.objects.create(
            owner=self.owner,
            name="Champions Test Turf",
            location="Latur",
            sport_type="cricket",
            description="Test turf",
            price_per_hour=800,
        )

    def test_active_turf_is_visible(self):
        response = self.client.get(
            reverse("turf_list")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Champions Test Turf",
        )

    def test_customer_cannot_add_turf(self):
        self.client.login(
            username="testcustomer",
            password="Customer@12345",
        )

        response = self.client.get(
            reverse("add_turf")
        )

        self.assertRedirects(
            response,
            reverse("home"),
        )

    def test_owner_can_add_slot(self):
        self.client.login(
            username="testowner",
            password="Owner@12345",
        )

        future_date = (
            timezone.localdate()
            + timedelta(days=1)
        )

        response = self.client.post(
            reverse(
                "add_slot",
                args=[self.turf.id],
            ),
            {
                "date": future_date,
                "start_time": "18:00",
                "end_time": "19:00",
            },
        )

        self.assertRedirects(
            response,
            reverse(
                "manage_slots",
                args=[self.turf.id],
            ),
        )

        self.assertTrue(
            Slot.objects.filter(
                turf=self.turf,
            ).exists()
        )

    def test_other_owner_cannot_edit_turf(self):
        self.client.login(
            username="otherowner",
            password="Other@12345",
        )

        response = self.client.get(
            reverse(
                "edit_turf",
                args=[self.turf.id],
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )