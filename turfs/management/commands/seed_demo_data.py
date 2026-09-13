import os
from datetime import time, timedelta

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from turfs.models import Slot, Sport, Turf


PICKLEBALL_TURFS = {
    "Pro Turf and Pro Pickleball",
    "The Score Saga - Cricket Turf & Pickleball",
    "Pitch and plate (TURF/ PICKLEBALL/ CAFE)",
}

SPECIAL_PRICE_TURFS = {
    "Marvel360 turf",
    "TURF TOWN",
    "Pro Turf and Pro Pickleball",
}

MORNING_SLOTS = [
    (time(6, 0), time(7, 0)),
    (time(7, 0), time(8, 0)),
    (time(8, 0), time(9, 0)),
]

EVENING_SLOTS = [
    (time(16, 0), time(17, 0)),
    (time(17, 0), time(18, 0)),
    (time(18, 0), time(20, 0)),
    (time(20, 0), time(21, 0)),
]


class Command(BaseCommand):
    help = "Create TurfPay demo data for a fresh database"

    def _required_env(self, name):
        value = os.environ.get(name)

        if not value:
            raise CommandError(
                f"Missing required environment variable: {name}"
            )

        return value

    @transaction.atomic
    def handle(self, *args, **options):
        admin_password = self._required_env(
            "TURFPAY_ADMIN_PASSWORD"
        )
        customer_password = self._required_env(
            "TURFPAY_CUSTOMER_PASSWORD"
        )
        owner_password = self._required_env(
            "TURFPAY_OWNER_PASSWORD"
        )

        self.stdout.write("Creating TurfPay demo data...")

        # Create the base Latur turf records.
        call_command("seed_latur_turfs")

        cricket, _ = Sport.objects.get_or_create(
            name="Cricket",
            slug="cricket",
        )
        football, _ = Sport.objects.get_or_create(
            name="Football",
            slug="football",
        )
        pickleball, _ = Sport.objects.get_or_create(
            name="Pickleball",
            slug="pickleball",
        )

        user_model = get_user_model()

        # Admin account.
        admin, _ = user_model.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@turfpay.local",
            },
        )
        admin.is_active = True
        admin.is_staff = True
        admin.is_superuser = True
        admin.set_password(admin_password)
        admin.save()

        # Five customer accounts.
        for number in range(1, 6):
            username = f"customer{number}"

            customer, _ = user_model.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"{username}@turfpay.local",
                },
            )
            customer.is_active = True
            customer.is_staff = False
            customer.is_superuser = False
            customer.set_password(customer_password)
            customer.save()

        today = timezone.localdate()

        # Configure every turf.
        for index, turf in enumerate(
            Turf.objects.order_by("id"),
            start=1,
        ):
            owner_username = (
                f"owner_{turf.name.lower()}"
                .replace("&", "and")
                .replace("/", "-")
                .replace("(", "")
                .replace(")", "")
                .replace(" ", "-")
            )
            owner_username = owner_username[:120]

            owner, _ = user_model.objects.get_or_create(
                username=owner_username,
                defaults={
                    "email": (
                        f"owner{index}@turfpay.local"
                    ),
                },
            )
            owner.is_active = True
            owner.is_staff = False
            owner.is_superuser = False
            owner.set_password(owner_password)
            owner.save()

            turf.owner = owner
            turf.price_per_hour = (
                1200
                if turf.name in SPECIAL_PRICE_TURFS
                else 1000
            )

            if not turf.opening_hours:
                turf.opening_hours = "Open 24 Hours"

            turf.is_active = True
            turf.save(
                update_fields=[
                    "owner",
                    "price_per_hour",
                    "opening_hours",
                    "is_active",
                ]
            )

            selected_sports = [
                cricket,
                football,
            ]

            if turf.name in PICKLEBALL_TURFS:
                selected_sports.append(pickleball)

            turf.sports.set(selected_sports)

            # Two future days of demo slots.
            for day_offset in (1, 2):
                slot_date = today + timedelta(
                    days=day_offset
                )

                for start_time, end_time in (
                    MORNING_SLOTS + EVENING_SLOTS
                ):
                    Slot.objects.get_or_create(
                        turf=turf,
                        date=slot_date,
                        start_time=start_time,
                        end_time=end_time,
                        defaults={
                            "is_available": True,
                        },
                    )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "TurfPay demo data is ready."
            )
        )
        self.stdout.write(
            f"Turfs: {Turf.objects.count()}"
        )
        self.stdout.write(
            f"Users: {user_model.objects.count()}"
        )
        self.stdout.write(
            f"Slots: {Slot.objects.count()}"
        )
        self.stdout.write("")
        self.stdout.write(
            "Demo usernames:"
        )
        self.stdout.write(
            "  Admin: admin"
        )
        self.stdout.write(
            "  Customers: customer1 - customer5"
        )
        self.stdout.write(
            "  Owners: owner-... (one per turf)"
        )
