from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import SlotForm, TurfForm
from .models import Slot, Sport, Turf


def turf_list(request):
    query = request.GET.get("q", "").strip()
    sport = request.GET.get("sport", "").strip()
    max_price = request.GET.get("max_price", "").strip()

    turfs = (
        Turf.objects
        .filter(is_active=True)
        .prefetch_related("sports")
    )

    if query:
        turfs = turfs.filter(
            Q(name__icontains=query)
            | Q(location__icontains=query)
            | Q(full_address__icontains=query)
            | Q(sports__name__icontains=query)
        )

    if sport:
        turfs = turfs.filter(
            sports__slug=sport
        )

    if max_price.isdigit():
        turfs = turfs.filter(
            price_per_hour__lte=int(max_price)
        )

    turfs = (
        turfs
        .distinct()
        .order_by(
            "-is_verified",
            "name",
        )
    )

    sports = Sport.objects.all()

    return render(
        request,
        "turfs/turf_list.html",
        {
            "turfs": turfs,
            "sports": sports,
            "query": query,
            "sport": sport,
            "max_price": max_price,
        },
    )


def turf_detail(request, pk):
    turf = get_object_or_404(
        Turf.objects.prefetch_related(
            "sports",
            "gallery_images",
        ),
        pk=pk,
        is_active=True,
    )

    now = timezone.localtime()
    today = now.date()

    current_time = now.time().replace(
        tzinfo=None
    )

    slots = (
        turf.slots
        .filter(is_available=True)
        .filter(
            Q(date__gt=today)
            | Q(
                date=today,
                start_time__gt=current_time,
            )
        )
        .order_by(
            "date",
            "start_time",
        )
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
def add_turf(request):
    if (
        not request.user.owned_turfs.exists()
        and not request.user.is_superuser
    ):
        return redirect("home")

    form = TurfForm(
        request.POST or None,
        request.FILES or None,
    )

    if (
        request.method == "POST"
        and form.is_valid()
    ):
        turf = form.save(
            commit=False
        )

        turf.owner = request.user
        turf.save()

        form.save_m2m()

        return redirect(
            "owner_dashboard"
        )

    return render(
        request,
        "turfs/turf_form.html",
        {
            "form": form,
            "title": "Add Turf",
        },
    )


@login_required
def edit_turf(request, turf_id):
    turf = get_object_or_404(
        Turf,
        pk=turf_id,
        owner=request.user,
    )

    form = TurfForm(
        request.POST or None,
        request.FILES or None,
        instance=turf,
    )

    if (
        request.method == "POST"
        and form.is_valid()
    ):
        form.save()

        return redirect(
            "owner_dashboard"
        )

    return render(
        request,
        "turfs/turf_form.html",
        {
            "form": form,
            "title": "Edit Turf",
            "turf": turf,
        },
    )


@login_required
def add_slot(request, turf_id):
    turf = get_object_or_404(
        Turf,
        pk=turf_id,
        owner=request.user,
    )

    form = SlotForm(
        request.POST or None
    )

    if (
        request.method == "POST"
        and form.is_valid()
    ):
        slot = form.save(
            commit=False
        )

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

    slots = (
        turf.slots
        .all()
        .order_by(
            "date",
            "start_time",
        )
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