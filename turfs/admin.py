from django.contrib import admin

from .models import Sport, Slot, Turf, TurfImage


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
        "slug",
    )


class TurfImageInline(admin.TabularInline):
    model = TurfImage
    extra = 1


@admin.register(Turf)
class TurfAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "sports_list",
        "price_per_hour",
        "owner",
        "is_verified",
        "is_active",
    )

    list_filter = (
        "sports",
        "is_verified",
        "is_active",
    )

    search_fields = (
        "name",
        "location",
        "full_address",
        "phone",
    )

    filter_horizontal = (
        "sports",
    )

    inlines = [
        TurfImageInline,
    ]

    @admin.display(
        description="Sports"
    )
    def sports_list(self, obj):
        return ", ".join(
            obj.sports.values_list(
                "name",
                flat=True,
            )
        )


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