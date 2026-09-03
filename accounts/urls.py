from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("owner/", views.owner_dashboard, name="owner_dashboard"),
    path("owner/bookings/", views.owner_bookings, name="owner_bookings"),
]