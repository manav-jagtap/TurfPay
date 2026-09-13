from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from bookings.models import Booking


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = UserCreationForm(
        request.POST or None
    )

    if (
        request.method == "POST"
        and form.is_valid()
    ):
        user = form.save()

        login(
            request,
            user,
        )

        return redirect("home")

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )


def is_owner(user):
    return (
        not user.is_superuser
        and user.owned_turfs.exists()
    )


@login_required
def owner_dashboard(request):
    if not is_owner(request.user):
        return HttpResponseForbidden(
            "Owner access only."
        )

    turfs = (
        request.user
        .owned_turfs
        .all()
    )

    return render(
        request,
        "accounts/owner_dashboard.html",
        {
            "turfs": turfs,
        },
    )


@login_required
def owner_bookings(request):
    if not is_owner(request.user):
        return HttpResponseForbidden(
            "Owner access only."
        )

    bookings = (
        Booking.objects
        .filter(
            slot__turf__owner=request.user
        )
        .select_related(
            "user",
            "slot",
            "slot__turf",
        )
        .order_by("-created_at")
    )

    return render(
        request,
        "accounts/owner_bookings.html",
        {
            "bookings": bookings,
        },
    )