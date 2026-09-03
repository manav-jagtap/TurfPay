from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from bookings.models import Booking


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "accounts/register.html", {"form": form})


@login_required
def owner_dashboard(request):
    turfs = request.user.owned_turfs.all()

    if not turfs.exists() and not request.user.is_superuser:
        return HttpResponseForbidden("Owner access only.")

    return render(
        request,
        "accounts/owner_dashboard.html",
        {"turfs": turfs},
    )

@login_required
def owner_bookings(request):
    bookings = Booking.objects.filter(
        slot__turf__owner=request.user
    ).select_related(
        "user",
        "slot",
        "slot__turf",
    ).order_by("-created_at")

    return render(
        request,
        "accounts/owner_bookings.html",
        {"bookings": bookings},
    )