from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_bookings, name="my_bookings"),
    path("slot/<int:slot_id>/", views.book_slot, name="book_slot"),
    path("<int:booking_id>/cancel/", views.cancel_booking, name="cancel_booking"),
]