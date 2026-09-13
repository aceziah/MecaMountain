from django.contrib import admin

from .models import Article, Category


# ==========================================================
# CATÉGORIES
# ==========================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

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


# ==========================================================
# ARTICLES
# ==========================================================

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "published_at",
        "is_published",
        "is_featured",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "content",
    )

    list_filter = (
        "category",
        "is_published",
        "is_featured",
        "published_at",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "-published_at",
        "-created_at",
    )

    fieldsets = (

        # ======================================================
        # INFORMATIONS GÉNÉRALES
        # ======================================================

        (
            "📰 Informations générales",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                )
            }
        ),

        # ======================================================
        # CONTENU
        # ======================================================

        (
            "📝 Contenu",
            {
                "fields": (
                    "short_description",
                    "content",
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
        # PUBLICATION
        # ======================================================

        (
            "📢 Publication",
            {
                "fields": (
                    "published_at",
                    "is_published",
                    "is_featured",
                )
            }
        ),

    )