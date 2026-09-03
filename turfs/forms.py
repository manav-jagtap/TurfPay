from django import forms

from .models import Slot, Turf


class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = [
            "name",
            "location",
            "sport_type",
            "description",
            "price_per_hour",
            "image",
        ]


class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = [
            "date",
            "start_time",
            "end_time",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "start_time": forms.TimeInput(
                attrs={"type": "time"}
            ),
            "end_time": forms.TimeInput(
                attrs={"type": "time"}
            ),
        }