from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Turf(models.Model):
    SPORT_CHOICES = [
        ("cricket", "Cricket"),
        ("football", "Football"),
        ("pickleball", "Pickleball"),
        ("multi", "Multi-sport"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_turfs",
        null=True,
        blank=True,
    )

    name = models.CharField(max_length=120)

    # Short locality shown on cards
    location = models.CharField(
        max_length=200
    )

    # Complete real-world address
    full_address = models.TextField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    sport_type = models.CharField(
        max_length=20,
        choices=SPORT_CHOICES,
        default="multi",
    )

    description = models.TextField(
        blank=True
    )

    # Main / cover image
    image = models.ImageField(
        upload_to="turfs/",
        blank=True,
        null=True,
    )

    price_per_hour = models.PositiveIntegerField()

    opening_hours = models.CharField(
        max_length=150,
        blank=True,
    )

    amenities = models.TextField(
        blank=True,
        help_text=(
            "Example: Floodlights, Parking, "
            "Changing Room, Drinking Water"
        ),
    )

    map_link = models.URLField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class TurfImage(models.Model):
    turf = models.ForeignKey(
        Turf,
        on_delete=models.CASCADE,
        related_name="gallery_images",
    )

    image = models.ImageField(
        upload_to="turfs/gallery/"
    )

    alt_text = models.CharField(
        max_length=150,
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.turf.name} Image"


class Slot(models.Model):
    turf = models.ForeignKey(
        Turf,
        on_delete=models.CASCADE,
        related_name="slots",
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    is_available = models.BooleanField(
        default=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "turf",
                    "date",
                    "start_time",
                    "end_time",
                ],
                name="unique_turf_slot",
            )
        ]

    def clean(self):
        if (
            self.date
            and self.date < timezone.localdate()
        ):
            raise ValidationError(
                {
                    "date": (
                        "Past dates are not allowed."
                    )
                }
            )

        if (
            self.start_time
            and self.end_time
            and self.end_time <= self.start_time
        ):
            raise ValidationError(
                {
                    "end_time": (
                        "End time must be later "
                        "than start time."
                    )
                }
            )

    def __str__(self):
        return (
            f"{self.turf.name} - "
            f"{self.date} {self.start_time}"
        )