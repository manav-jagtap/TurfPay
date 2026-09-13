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
            "sports",
            "description",
            "image",
            "price_per_hour",
            "opening_hours",
            "amenities",
            "map_link",
            "website",
        ]

        widgets = {
            "sports": forms.CheckboxSelectMultiple(),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Describe the turf",
                }
            ),

            "full_address": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Enter complete turf address",
                }
            ),

            "amenities": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": (
                        "Example: Floodlights, Parking, "
                        "Changing Room"
                    ),
                }
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
                attrs={
                    "type": "date",
                }
            ),

            "start_time": forms.TimeInput(
                attrs={
                    "type": "time",
                }
            ),

            "end_time": forms.TimeInput(
                attrs={
                    "type": "time",
                }
            ),
        }