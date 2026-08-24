from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q


class Project(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", "En cours"
        COMPLETED = "COMPLETED", "Terminé"
        ARCHIVED = "ARCHIVED", "Archivé"

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    short_description = models.CharField(max_length=250)

    category = models.ForeignKey("ProjectCategory",
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
    
    description = models.TextField()

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

# permettant l'ajout de la checkbox "Projet visible dans la page d'accueil" au sein de Django admin
    show_on_homepage = models.BooleanField(
        default=False,
        verbose_name="Projet visible sur la page d'accueil"
    )

# On maximise le nombre de project définit à 4 sur la page d'accueil et de plus, il doit aussi être définit comme visible dans mes projets
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title