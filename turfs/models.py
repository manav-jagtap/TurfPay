from django.db import models


class Turf(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=200)
    price_per_hour = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Slot(models.Model):
    turf = models.ForeignKey(
        Turf,
        on_delete=models.CASCADE,
        related_name="slots"
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.turf.name} - {self.date} {self.start_time}"