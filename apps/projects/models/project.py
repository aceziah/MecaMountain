from django.db import models


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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title