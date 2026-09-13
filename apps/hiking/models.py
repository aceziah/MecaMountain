from django.db import models
from django.urls import reverse

class Equipment(models.Model):

    name = models.CharField(
        "Nom",
        max_length=100,
    )

    slug = models.SlugField(
        "Slug",
        unique=True,
    )

    image = models.ImageField(
        "Image",
        upload_to="equipment/",
        blank=True,
        null=True,
    )

    description = models.TextField(
        "Description",
        blank=True,
    )

    def __str__(self):
        return self.name

    
class Hiking(models.Model):

    # ==========================================================
    # INFORMATIONS GÉNÉRALES
    # ==========================================================

    title = models.CharField(
        max_length=200,
        verbose_name="Nom",
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="Slug",
    )

    location = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Lieu",
    )

    massif = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Massif / secteur",
    )

    date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date",
    )


    # ==========================================================
    # DESCRIPTION
    # ==========================================================

    short_description = models.TextField(
        blank=True,
        verbose_name="Description courte",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    equipment = models.ManyToManyField(
    Equipment,
    blank=True,
    related_name="hikings",
    verbose_name="Équipements",
    )


    # ==========================================================
    # CARACTÉRISTIQUES
    # ==========================================================

    distance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Distance (km)",
    )

    elevation_gain = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Dénivelé positif (m)",
    )

    max_altitude = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Altitude maximale (m)",
    )

    duration = models.DurationField(
        blank=True,
        null=True,
        verbose_name="Durée",
    )

    DIFFICULTY_CHOICES = [
        ("facile", "Facile"),
        ("moderee", "Modérée"),
        ("difficile", "Difficile"),
        ("tres_difficile", "Très difficile"),
    ]

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        blank=True,
        verbose_name="Difficulté",
    )

    # ==========================================================
    # VISUEL
    # ==========================================================

    thumbnail = models.ImageField(
        upload_to="hiking/thumbnails/",
        blank=True,
        null=True,
        verbose_name="Image principale",
    )


    # ==========================================================
    # LIEN GPS
    # ==========================================================

    gpx_url = models.URLField(
        blank=True,
        verbose_name="Lien GPX",
    )


    # ==========================================================
    # PUBLICATION
    # ==========================================================

    is_featured = models.BooleanField(
        default=False,
        verbose_name="Mettre en avant",
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name="Publié",
    )


    # ==========================================================
    # MÉTHODES
    # ==========================================================

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse(
            "hiking:detail",
            kwargs={"slug": self.slug},
        )



class HikingImage(models.Model):

    hiking = models.ForeignKey(
        Hiking,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Randonnée",
    )

    image = models.ImageField(
        upload_to="hiking/gallery/",
        verbose_name="Image",
    )

    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Légende",
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre",
    )


    class Meta:
        ordering = ["order"]


    def __str__(self):
        return f"{self.hiking.title} — {self.title}"