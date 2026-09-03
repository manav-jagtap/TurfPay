from django.conf import settings
from django.db import models
from django.db.models import Q
from turfs.models import Slot


class Booking(models.Model):
    STATUS_CHOICES = [
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="confirmed",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["slot"],
                condition=Q(status="confirmed"),
                name="unique_confirmed_booking_per_slot",
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.slot}"