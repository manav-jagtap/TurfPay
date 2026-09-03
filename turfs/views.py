from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import SlotForm
from .models import Slot, Turf


def turf_list(request):
    query = request.GET.get("q", "").strip()
    sport = request.GET.get("sport", "").strip()
    max_price = request.GET.get("max_price", "").strip()

    turfs = Turf.objects.filter(is_active=True)

    if query:
        turfs = turfs.filter(
            Q(name__icontains=query)
            | Q(location__icontains=query)
        )

    if sport:
        turfs = turfs.filter(sport_type=sport)

    if max_price.isdigit():
        turfs = turfs.filter(
            price_per_hour__lte=int(max_price)
        )

    return render(
        request,
        "turfs/turf_list.html",
        {
            "turfs": turfs,
            "query": query,
            "sport": sport,
            "max_price": max_price,
        },
    )


def turf_detail(request, pk):
    turf = get_object_or_404(
        Turf,
        pk=pk,
        is_active=True,
    )

    now = timezone.localtime()
    today = now.date()
    current_time = now.time().replace(tzinfo=None)

    slots = turf.slots.filter(
        is_available=True,
    ).filter(
        Q(date__gt=today)
        | Q(
            date=today,
            start_time__gt=current_time,
        )
    ).order_by(
        "date",
        "start_time",
    )

    return render(
        request,
        "turfs/turf_detail.html",
        {
            "turf": turf,
            "slots": slots,
        },
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

        return redirect(
            "manage_slots",
            turf_id=turf.id,
        )

    return render(
        request,
        "turfs/add_slot.html",
        {
            "form": form,
            "turf": turf,
        },
    )


@login_required
def manage_slots(request, turf_id):
    turf = get_object_or_404(
        Turf,
        pk=turf_id,
        owner=request.user,
    )

    slots = turf.slots.all().order_by(
        "date",
        "start_time",
    )

    return render(
        request,
        "turfs/manage_slots.html",
        {
            "turf": turf,
            "slots": slots,
        },
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

    if (
        request.method == "POST"
        and not slot.booking_set.exists()
    ):
        slot.delete()

    return redirect(
        "manage_slots",
        turf_id=turf_id,
    )