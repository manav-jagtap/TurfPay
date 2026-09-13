from urllib.parse import quote_plus

from django.core.management.base import BaseCommand

from turfs.models import Sport, Turf


class Command(BaseCommand):
    help = "Import initial Latur turf venues into TurfPay"

    def handle(self, *args, **options):
        cricket, _ = Sport.objects.get_or_create(
            name="Cricket",
            slug="cricket",
        )

        football, _ = Sport.objects.get_or_create(
            name="Football",
            slug="football",
        )

        pickleball, _ = Sport.objects.get_or_create(
            name="Pickleball",
            slug="pickleball",
        )

        sport_map = {
            "cricket": cricket,
            "football": football,
            "pickleball": pickleball,
        }

        turf_data = [
            {
                "name": "Pro Turf and Pro Pickleball",
                "location": "Deep Jyoti Nagar",
                "full_address": (
                    "Deep Jyoti Nagar, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [
                    "pickleball",
                ],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports venue in Latur with "
                    "turf and pickleball facilities."
                ),
            },
            {
                "name": (
                    "The Score Saga - "
                    "Cricket Turf & Pickleball"
                ),
                "location": "Ausa Ring Road",
                "full_address": (
                    "Ausa Ring Road, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [
                    "cricket",
                    "pickleball",
                ],
                "opening_hours": "",
                "amenities": (
                    "Synthetic Turf, Floodlights"
                ),
                "description": (
                    "Sports venue offering cricket "
                    "and pickleball facilities."
                ),
            },
            {
                "name": "DADAJI TURF",
                "location": "Latur",
                "full_address": (
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports turf located in Latur."
                ),
            },
            {
                "name": "Nishu sports legacy",
                "location": "Katpur Road",
                "full_address": (
                    "Katpur Road, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [
                    "cricket",
                    "football",
                ],
                "opening_hours": "",
                "amenities": (
                    "Cricket Turf, Football Turf"
                ),
                "description": (
                    "Sports facility with cricket "
                    "and football turf facilities."
                ),
            },
            {
                "name": "Kick off turf",
                "location": "Latur",
                "full_address": (
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports turf located in Latur."
                ),
            },
            {
                "name": "Marvel360 turf",
                "location": "Latur",
                "full_address": (
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports turf located in Latur."
                ),
            },
            {
                "name": "TURF TOWN",
                "location": "Latur",
                "full_address": (
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports turf located in Latur."
                ),
            },
            {
                "name": "Strikers sports club",
                "location": "Sawe Wadi",
                "full_address": (
                    "Sawe Wadi, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports club and turf facility "
                    "in Latur."
                ),
            },
            {
                "name": "Grand Slam",
                "location": "Signal Camp",
                "full_address": (
                    "Signal Camp, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports venue located in Latur."
                ),
            },
            {
                "name": "RIELITE CRICKET TURF",
                "location": "Ausekar Nagar",
                "full_address": (
                    "Ausekar Nagar, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [
                    "cricket",
                ],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Cricket turf located in Latur."
                ),
            },
            {
                "name": "Birla protruf",
                "location": "Latur",
                "full_address": (
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports turf facility in Latur."
                ),
            },
            {
                "name": "The Battle Square Turff",
                "location": "Latur MIDC",
                "full_address": (
                    "Latur MIDC, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Outdoor sports turf facility "
                    "in Latur."
                ),
            },
            {
                "name": (
                    "Pitch and plate "
                    "(TURF/ PICKLEBALL/ CAFE)"
                ),
                "location": "Ausa - Latur Road",
                "full_address": (
                    "Ausa - Latur Road, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [
                    "pickleball",
                ],
                "opening_hours": "",
                "amenities": (
                    "Turf, Pickleball, Cafe"
                ),
                "description": (
                    "Sports venue with turf, "
                    "pickleball and cafe facilities."
                ),
            },
            {
                "name": "CricZone Turf Latur",
                "location": "Ring Road",
                "full_address": (
                    "Ring Road, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [
                    "cricket",
                ],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports turf located in Latur."
                ),
            },
            {
                "name": "CHOUDHARY TURF",
                "location": "Sarola Road",
                "full_address": (
                    "Sarola Road, "
                    "Latur, Maharashtra"
                ),
                "phone": "",
                "sports": [],
                "opening_hours": "",
                "amenities": "",
                "description": (
                    "Sports turf located in Latur."
                ),
            },
        ]

        created_count = 0
        existing_count = 0

        for data in turf_data:
            sport_slugs = data["sports"]

            map_link = (
                "https://www.google.com/maps/"
                "search/?api=1&query="
                + quote_plus(
                    data["full_address"]
                )
            )

            turf, created = Turf.objects.get_or_create(
                name=data["name"],
                defaults={
                    "location": data["location"],
                    "full_address": data["full_address"],
                    "phone": data["phone"],
                    "description": data["description"],
                    "price_per_hour": None,
                    "opening_hours": data["opening_hours"],
                    "amenities": data["amenities"],
                    "map_link": map_link,
                    "is_verified": False,
                    "is_active": True,
                },
            )

            if created:
                created_count += 1

            else:
                existing_count += 1

                update_fields = []

                fillable_fields = {
                    "location": data["location"],
                    "full_address": data["full_address"],
                    "phone": data["phone"],
                    "description": data["description"],
                    "opening_hours": data["opening_hours"],
                    "amenities": data["amenities"],
                    "map_link": map_link,
                }

                for field, value in fillable_fields.items():
                    if (
                        value
                        and not getattr(turf, field)
                    ):
                        setattr(
                            turf,
                            field,
                            value,
                        )

                        update_fields.append(
                            field
                        )

                if update_fields:
                    turf.save(
                        update_fields=update_fields
                    )

            if (
                sport_slugs
                and not turf.sports.exists()
            ):
                turf.sports.set(
                    [
                        sport_map[slug]
                        for slug in sport_slugs
                    ]
                )

            sports_text = ", ".join(
                turf.sports.values_list(
                    "name",
                    flat=True,
                )
            )

            if not sports_text:
                sports_text = (
                    "Awaiting sport confirmation"
                )

            status = (
                "Created"
                if created
                else "Existing"
            )

            self.stdout.write(
                f"{status}: "
                f"{turf.name} "
                f"[{sports_text}]"
            )

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                (
                    "Import complete. "
                    f"Created: {created_count}, "
                    f"Existing: {existing_count}"
                )
            )
        )