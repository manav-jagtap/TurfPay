from django.contrib import admin

from .models import Slot, Turf, TurfImage


class TurfImageInline(admin.TabularInline):
    model = TurfImage
    extra = 1


@admin.register(Turf)
class TurfAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "sport_type",
        "price_per_hour",
        "owner",
        "is_verified",
        "is_active",
    )

    list_filter = (
        "sport_type",
        "is_verified",
        "is_active",
    )

    search_fields = (
        "name",
        "location",
        "full_address",
        "phone",
    )

    inlines = [
        TurfImageInline,
    ]


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = (
        "turf",
        "date",
        "start_time",
        "end_time",
        "is_available",
    )

    list_filter = (
        "date",
        "is_available",
    )

    search_fields = (
        "turf__name",
    )


@admin.register(TurfImage)
class TurfImageAdmin(admin.ModelAdmin):
    list_display = (
        "turf",
        "order",
        "alt_text",
    )