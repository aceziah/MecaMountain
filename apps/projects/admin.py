from django.contrib import admin
from django.template.response import TemplateResponse
from django.db import transaction
from .models import (
    Project,
    Technology,
    ProjectCategory,
    ProjectImage,
    HomepageProjectOrder,
    ProjectPageOrder,
)


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


# ==========================================================
# ORDRE D'AFFICHAGE ACCUEIL
# ==========================================================

@admin.register(HomepageProjectOrder)
class HomepageProjectOrderAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):

        queryset = self.get_queryset(request)

        if request.method == "POST":

            project_ids = request.POST.getlist("project_ids")

            valid_ids = set(
                str(project.pk)
                for project in queryset
            )

            submitted_ids = set(project_ids)

            if (
                len(project_ids) == queryset.count()
                and submitted_ids == valid_ids
            ):

                with transaction.atomic():

                    for order, project_id in enumerate(
                        project_ids,
                        start=1,
                    ):

                        Project.objects.filter(
                            pk=project_id,
                            show_on_homepage=True,
                        ).update(
                            homepage_order=order
                        )

                self.message_user(
                    request,
                    "L'ordre d'affichage de l'accueil a été enregistré.",
                    level="success",
                )

            else:

                self.message_user(
                    request,
                    "Impossible d'enregistrer l'ordre des projets.",
                    level="error",
                )

        projects = self.get_queryset(request)

        context = {
            **self.admin_site.each_context(request),
            "title": "Ordre d'affichage Accueil",
            "projects": projects,
        }

        return TemplateResponse(
            request,
            "admin/projects/homepage_order.html",
            context,
        )

    def get_queryset(self, request):

        return super().get_queryset(request).filter(
            show_on_homepage=True
        ).order_by(
            "homepage_order",
            "pk",
        )


# ==========================================================
# ORDRE D'AFFICHAGE PROJET
# ==========================================================

@admin.register(ProjectPageOrder)
class ProjectPageOrderAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):

        queryset = self.get_queryset(request)

        if request.method == "POST":

            project_ids = request.POST.getlist("project_ids")

            valid_ids = set(
                str(project.pk)
                for project in queryset
            )

            submitted_ids = set(project_ids)

            if (
                len(project_ids) == queryset.count()
                and submitted_ids == valid_ids
            ):

                with transaction.atomic():

                    for order, project_id in enumerate(
                        project_ids,
                        start=1,
                    ):

                        Project.objects.filter(
                            pk=project_id,
                            is_featured=True,
                        ).update(
                            project_order=order
                        )

                self.message_user(
                    request,
                    "L'ordre d'affichage des projets a été enregistré.",
                    level="success",
                )

            else:

                self.message_user(
                    request,
                    "Impossible d'enregistrer l'ordre des projets.",
                    level="error",
                )

        projects = self.get_queryset(request)

        context = {
            **self.admin_site.each_context(request),
            "title": "Ordre d'affichage Projet",
            "projects": projects,
        }

        return TemplateResponse(
            request,
            "admin/projects/project_order.html",
            context,
        )

    def get_queryset(self, request):

        return super().get_queryset(request).filter(
            is_featured=True
        ).order_by(
            "project_order",
            "pk",
        )