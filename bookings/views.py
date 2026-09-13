from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from turfs.models import Slot
from .models import Booking


def is_customer(user):
    return (
        user.is_authenticated
        and not user.is_superuser
        and not user.owned_turfs.exists()
    )


def same_time_slots(slot):
    """
    Return every DB row representing the same real-world turf time.
    This protects us even if old seed data created duplicate Slot rows.
    """
    return Slot.objects.filter(
        turf_id=slot.turf_id,
        date=slot.date,
        start_time=slot.start_time,
        end_time=slot.end_time,
    )


@login_required
def book_slot(request, slot_id):
    if not is_customer(request.user):
        return HttpResponseForbidden("Customer access only.")

    if request.method != "POST":
        return redirect("turf_list")

    turf_id = None

    try:
        with transaction.atomic():
            slot = get_object_or_404(
                Slot.objects.select_for_update().select_related("turf"),
                pk=slot_id,
            )
            turf_id = slot.turf_id

            logical_slots = Slot.objects.select_for_update().filter(
                turf_id=slot.turf_id,
                date=slot.date,
                start_time=slot.start_time,
                end_time=slot.end_time,
            )

            logical_slot_ids = list(
                logical_slots.values_list("id", flat=True)
            )

            already_booked = Booking.objects.filter(
                slot_id__in=logical_slot_ids,
                status="confirmed",
            ).exists()

            if already_booked or not slot.is_available:
                logical_slots.update(is_available=False)

                messages.error(
                    request,
                    "This time slot is already booked. Please choose another slot.",
                )
                return redirect("turf_detail", pk=slot.turf_id)

            Booking.objects.create(
                user=request.user,
                slot=slot,
                status="confirmed",
            )

            # Mark every duplicate DB row for this real-world time unavailable.
            logical_slots.update(is_available=False)

    except IntegrityError:
        messages.error(
            request,
            "This time slot was just booked by another customer. "
            "Please choose another slot.",
        )
        if turf_id is not None:
            return redirect("turf_detail", pk=turf_id)
        return redirect("turf_list")

    messages.success(request, "Booking confirmed successfully.")
    return redirect("my_bookings")


@login_required
def my_bookings(request):
    if not is_customer(request.user):
        return HttpResponseForbidden("Customer access only.")

    bookings = (
        Booking.objects
        .filter(user=request.user)
        .select_related("slot", "slot__turf")
        .order_by("-created_at")
    )

    return render(
        request,
        "bookings/my_bookings.html",
        {"bookings": bookings},
    )


@login_required
def cancel_booking(request, booking_id):
    if not is_customer(request.user):
        return HttpResponseForbidden("Customer access only.")

    if request.method != "POST":
        return redirect("my_bookings")

    with transaction.atomic():
        booking = get_object_or_404(
            Booking.objects.select_for_update().select_related("slot"),
            pk=booking_id,
            user=request.user,
            status="confirmed",
        )

        slot = Slot.objects.select_for_update().get(pk=booking.slot_id)

        logical_slots = Slot.objects.select_for_update().filter(
            turf_id=slot.turf_id,
            date=slot.date,
            start_time=slot.start_time,
            end_time=slot.end_time,
        )

        logical_slot_ids = list(
            logical_slots.values_list("id", flat=True)
        )

        booking.status = "cancelled"
        booking.save(update_fields=["status"])

        still_confirmed = Booking.objects.filter(
            slot_id__in=logical_slot_ids,
            status="confirmed",
        ).exists()

        if still_confirmed:
            logical_slots.update(is_available=False)
        else:
            logical_slots.update(is_available=True)

    messages.success(
        request,
        "Booking cancelled successfully. The slot is available again.",
    )
    return redirect("my_bookings")
