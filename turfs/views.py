from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SlotForm
from .models import Turf
from .models import Slot, Turf

def turf_list(request):
    turfs = Turf.objects.filter(is_active=True)
    return render(request, "turfs/turf_list.html", {"turfs": turfs})


def turf_detail(request, pk):
    turf = get_object_or_404(Turf, pk=pk, is_active=True)
    slots = turf.slots.filter(is_available=True).order_by("date", "start_time")

    return render(
        request,
        "turfs/turf_detail.html",
        {"turf": turf, "slots": slots},
    )


@login_required
def add_slot(request, turf_id):
    turf = get_object_or_404(
        Turf,
        pk=turf_id,
        owner=request.user,
    )

    form = SlotForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        slot = form.save(commit=False)
        slot.turf = turf
        slot.save()

        return redirect("owner_dashboard")

    return render(
        request,
        "turfs/add_slot.html",
        {"form": form, "turf": turf},
    )

@login_required
def manage_slots(request, turf_id):
    turf = get_object_or_404(
        Turf,
        pk=turf_id,
        owner=request.user,
    )

    slots = turf.slots.all().order_by("date", "start_time")

    return render(
        request,
        "turfs/manage_slots.html",
        {"turf": turf, "slots": slots},
    )

@login_required
def delete_slot(request, slot_id):
    slot = get_object_or_404(
        Slot,
        pk=slot_id,
        turf__owner=request.user,
        is_available=True,
    )

    turf_id = slot.turf_id

    if request.method == "POST" and not slot.booking_set.exists():
        slot.delete()

    return redirect("manage_slots", turf_id=turf_id)