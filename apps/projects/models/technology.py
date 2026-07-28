from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Technologie"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name