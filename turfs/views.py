from django.shortcuts import render, get_object_or_404
from .models import Turf


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