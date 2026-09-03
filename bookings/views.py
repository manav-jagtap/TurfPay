from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from turfs.models import Slot
from .models import Booking


@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(
        Slot,
        pk=slot_id,
        is_available=True,
    )

    if request.method == "POST":
        Booking.objects.create(
            user=request.user,
            slot=slot,
        )

        slot.is_available = False
        slot.save(update_fields=["is_available"])

    return redirect("turf_detail", pk=slot.turf_id)


@login_required
def my_bookings(request):
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
    booking = get_object_or_404(
        Booking,
        pk=booking_id,
        user=request.user,
        status="confirmed",
    )

    if request.method == "POST":
        booking.status = "cancelled"
        booking.save(update_fields=["status"])

        booking.slot.is_available = True
        booking.slot.save(update_fields=["is_available"])

    return redirect("my_bookings")