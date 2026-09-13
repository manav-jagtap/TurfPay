from django import forms

from .models import Slot, Turf


class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf

        fields = [
            "name",
            "location",
            "full_address",
            "phone",
            "sport_type",
            "description",
            "image",
            "price_per_hour",
            "opening_hours",
            "amenities",
            "map_link",
            "website",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 4}
            ),
            "amenities": forms.Textarea(
                attrs={"rows": 3}
            ),
            "full_address": forms.Textarea(
                attrs={"rows": 3}
            ),
        }


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