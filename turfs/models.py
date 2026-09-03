from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Turf(models.Model):
    SPORT_CHOICES = [
        ("cricket", "Cricket"),
        ("football", "Football"),
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
    location = models.CharField(max_length=200)

    sport_type = models.CharField(
        max_length=20,
        choices=SPORT_CHOICES,
        default="multi",
    )

    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="turfs/",
        blank=True,
        null=True,
    )

    price_per_hour = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Slot(models.Model):
    turf = models.ForeignKey(
        Turf,
        on_delete=models.CASCADE,
        related_name="slots",
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    is_available = models.BooleanField(default=True)

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
        if self.date and self.date < timezone.localdate():
            raise ValidationError(
                {
                    "date": "Past dates are not allowed."
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
                        "End time must be later than start time."
                    )
                }
            )

    def __str__(self):
        return (
            f"{self.turf.name} - "
            f"{self.date} {self.start_time}"
        )