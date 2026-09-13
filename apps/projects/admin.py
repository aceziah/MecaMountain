from django.contrib import admin

from .models import Project, Technology, ProjectCategory, ProjectImage


# ==========================================================
# IMAGES DES PROJETS
# ==========================================================

class ProjectImageInline(admin.TabularInline):

    model = ProjectImage

    # Une ligne vide pour ajouter une nouvelle image
    extra = 1


# ==========================================================
# PROJETS
# ==========================================================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "is_featured",
        "show_on_homepage",
    )

    search_fields = (
        "title",
        "short_description",
    )

    list_filter = (
        "category",
        "status",
        "is_featured",
        "show_on_homepage",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "technologies",
    )

    inlines = [
        ProjectImageInline,
    ]

    ordering = (
        "title",
    )

    fieldsets = (

        # ======================================================
        # INFORMATIONS GÉNÉRALES
        # ======================================================

        (
            "📌 Informations générales",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "status",
                )
            }
        ),

        # ======================================================
        # CONTENU DU PROJET
        # ======================================================

        (
            "📝 Contenu du projet",
            {
                "fields": (
                    "short_description",
                    "description",
                    "idea",
                    "conception",
                    "realisation",
                    "resultat",
                )
            }
        ),

        # ======================================================
        # TECHNOLOGIES
        # ======================================================

        (
            "🔧 Technologies",
            {
                "fields": (
                    "technologies",
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
        # LIENS
        # ======================================================

        (
            "🔗 Liens",
            {
                "fields": (
                    "github_url",
                    "demo_url",
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
                    "is_featured",
                    "show_on_homepage",
                )
            }
        ),

    )

# ==========================================================
# TECHNOLOGIES
# ==========================================================

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


# ==========================================================
# CATÉGORIES
# ==========================================================

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


# ==========================================================
# IMAGES
# ==========================================================

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "title",
        "order",
    )

    list_filter = (
        "project",
    )

    ordering = (
        "project",
        "order",
    )