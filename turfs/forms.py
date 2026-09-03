from django import forms

from .models import Slot


class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ["date", "start_time", "end_time"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }