from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from turfs.models import Slot
from .models import Booking


@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(Slot, pk=slot_id, is_available=True)

    if request.method == "POST":
        Booking.objects.create(user=request.user, slot=slot)

        slot.is_available = False
        slot.save(update_fields=["is_available"])

        return redirect("turf_detail", pk=slot.turf_id)

    return redirect("turf_detail", pk=slot.turf_id)