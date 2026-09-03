from django.urls import path

from . import views

urlpatterns = [
    path("", views.turf_list, name="turf_list"),
    path("<int:pk>/", views.turf_detail, name="turf_detail"),
    path(
        "<int:turf_id>/slots/add/",
        views.add_slot,
        name="add_slot",
    ),
    path(
    "<int:turf_id>/slots/",
    views.manage_slots,
    name="manage_slots",
    ),path(
    "slots/<int:slot_id>/delete/",
    views.delete_slot,
    name="delete_slot",
),

]