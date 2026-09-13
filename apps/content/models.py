from django.db import models
from django.urls import reverse


# ==========================================================
# CATÉGORIES D'ARTICLES
# ==========================================================

class Category(models.Model):

    name = models.CharField(
        "Nom",
        max_length=100,
    )

    slug = models.SlugField(
        "Slug",
        unique=True,
    )

    description = models.TextField(
        "Description",
        blank=True,
    )

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["name"]

    def __str__(self):
        return self.name


# ==========================================================
# ARTICLES
# ==========================================================

class Article(models.Model):

    # ======================================================
    # INFORMATIONS GÉNÉRALES
    # ======================================================

    title = models.CharField(
        "Titre",
        max_length=200,
    )

    slug = models.SlugField(
        "Slug",
        unique=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="articles",
        verbose_name="Catégorie",
    )

    # ======================================================
    # CONTENU
    # ======================================================

    short_description = models.TextField(
        "Description courte",
        blank=True,
    )

    content = models.TextField(
        "Contenu",
    )

    # ======================================================
    # IMAGE
    # ======================================================

    thumbnail = models.ImageField(
        "Image principale",
        upload_to="articles/thumbnails/",
        blank=True,
        null=True,
    )

    # ======================================================
    # PUBLICATION
    # ======================================================

    published_at = models.DateTimeField(
        "Date de publication",
        blank=True,
        null=True,
    )

    is_featured = models.BooleanField(
        "Mettre en avant",
        default=False,
    )

    is_published = models.BooleanField(
        "Publié",
        default=True,
    )

    # ======================================================
    # DATES TECHNIQUES
    # ======================================================

    created_at = models.DateTimeField(
        "Date de création",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        "Dernière modification",
        auto_now=True,
    )

    # ======================================================
    # META
    # ======================================================

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-published_at", "-created_at"]

    # ======================================================
    # MÉTHODES
    # ======================================================

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "content:article_detail",
            kwargs={"slug": self.slug},
        )