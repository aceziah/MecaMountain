from django.contrib import admin

from .models import Project, Technology, ProjectCategory, ProjectImage

# Register your models here.
# admin.site.register(Project)
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
# Ouvrir un projet --> Django affichera automatiquement une ligne vide pour ajouter une nouvelle image.
    extra = 1
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "is_featured",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "short_description",
    )

    list_filter = (
        "category",
        "status",
        "is_featured",
        "created_at",
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
        "-created_at",
    )


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
        list_display = ("name", "slug")
        search_fields = ("name",)
        prepopulated_fields = {
        "slug": ("name",)
    }

        @admin.register(ProjectCategory)
        class ProjectCategoryAdmin(admin.ModelAdmin):
            list_display = ("name", "slug")
            search_fields = ("name",)
            prepopulated_fields = {
            "slug": ("name",)
        }
        
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