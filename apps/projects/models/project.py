from django.db import models
from django.core.exceptions import ValidationError


class Project(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", "En cours"
        COMPLETED = "COMPLETED", "Terminé"
        ARCHIVED = "ARCHIVED", "Archivé"

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    short_description = models.CharField(max_length=250)

    category = models.ForeignKey(
        "ProjectCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects",
    )

    technologies = models.ManyToManyField(
        "Technology",
        blank=True,
        related_name="projects",
    )

    description = models.TextField(
        verbose_name="À propos du projet"
    )

    idea = models.TextField(
        blank=True,
        verbose_name="01 — L'idée"
    )

    conception = models.TextField(
        blank=True,
        verbose_name="02 — La conception"
    )

    realisation = models.TextField(
        blank=True,
        verbose_name="03 — La réalisation"
    )

    resultat = models.TextField(
        blank=True,
        verbose_name="04 — Le résultat"
    )

    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/",
        blank=True,
        null=True,
    )

    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.IN_PROGRESS,
    )

    is_featured = models.BooleanField(default=False)

    # Permet l'ajout de la checkbox
    # "Projet visible sur la page d'accueil" dans Django Admin
    show_on_homepage = models.BooleanField(
        default=False,
        verbose_name="Projet visible sur la page d'accueil"
    )

    # Un projet doit être visible sur le site pour pouvoir
    # être affiché sur la page d'accueil.
    # Maximum 4 projets peuvent être affichés sur la page d'accueil.
    def clean(self):
        super().clean()

        if self.show_on_homepage and not self.is_featured:
            raise ValidationError({
                "show_on_homepage": (
                    "Un projet doit être visible sur le site "
                    "avant de pouvoir être affiché sur la page d'accueil."
                )
            })

        if self.show_on_homepage:
            homepage_projects = Project.objects.filter(
                show_on_homepage=True
            ).exclude(pk=self.pk)

            if homepage_projects.count() >= 4:
                raise ValidationError({
                    "show_on_homepage": (
                        "Maximum de 4 projets peuvent être affichés "
                        "sur la page d'accueil."
                    )
                })

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title