from django.contrib import admin

from .models import Hiking, HikingImage, Equipment


# ==========================================================
# IMAGES DES RANDONNÉES
# ==========================================================

class HikingImageInline(admin.TabularInline):

    model = HikingImage

    extra = 1


# ==========================================================
# RANDONNÉES
# ==========================================================

@admin.register(Hiking)
class HikingAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "location",
        "massif",
        "difficulty",
        "date",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "location",
        "massif",
        "short_description",
    )

    list_filter = (
        "difficulty",
        "massif",
        "is_featured",
        "is_published",
        "date",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "equipment",
    )

    inlines = [
        HikingImageInline,
    ]

    ordering = (
        "-date",
    )

    fieldsets = (

        # ======================================================
        # INFORMATIONS GÉNÉRALES
        # ======================================================

        (
            "🥾 Informations générales",
            {
                "fields": (
                    "title",
                    "slug",
                    "location",
                    "massif",
                    "date",
                )
            }
        ),

        # ======================================================
        # DESCRIPTION
        # ======================================================

        (
            "📝 Description",
            {
                "fields": (
                    "short_description",
                    "description",
                )
            }
        ),

        # ======================================================
        # ÉQUIPEMENTS
        # ======================================================

        (
            "🎒 Équipements",
            {
                "fields": (
                    "equipment",
                )
            }
        ),


        # ======================================================
        # CARACTÉRISTIQUES
        # ======================================================

        (
            "📊 Caractéristiques",
            {
                "fields": (
                    "distance",
                    "elevation_gain",
                    "max_altitude",
                    "duration",
                    "difficulty",
                )
            }
        ),

        # ======================================================
        # VISUEL
        # ======================================================

        (
            "🖼️ Visuel",
            {
                "fields": (
                    "thumbnail",
                )
            }
        ),

        # ======================================================
        # GPS
        # ======================================================

        (
            "🗺️ GPS",
            {
                "fields": (
                    "gpx_url",
                )
            }
        ),

        # ======================================================
        # PUBLICATION
        # ======================================================

        (
            "📢 Publication",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                )
            }
        ),

    )


# ==========================================================
# IMAGES
# ==========================================================

@admin.register(HikingImage)
class HikingImageAdmin(admin.ModelAdmin):

    list_display = (
        "hiking",
        "title",
        "order",
    )

    list_filter = (
        "hiking",
    )

    ordering = (
        "hiking",
        "order",
    )

# ==========================================================
# ÉQUIPEMENTS
# ==========================================================

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "name",
    )