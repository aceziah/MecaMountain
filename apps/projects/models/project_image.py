from django.db import models


class ProjectImage(models.Model):
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(upload_to="projects/images/")

    title = models.CharField(
        max_length=100,
        blank=True,
    )

    alt_text = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Texte alternatif",
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage",
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.title} ({self.order})"