from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.projects.models import Project


class ProjectModelTests(TestCase):

    def test_homepage_project_must_be_featured(self):
        project = Project(
            title="Projet test",
            slug="projet-test",
            short_description="Description test",
            description="Description complète du projet.",
            is_featured=False,
            show_on_homepage=True,
        )

        with self.assertRaises(ValidationError):
            project.full_clean()

    def test_featured_project_can_be_on_homepage(self):
        project = Project(
            title="Projet test",
            slug="projet-test",
            short_description="Description test",
            description="Description complète du projet.",
            is_featured=True,
            show_on_homepage=True,
        )

        project.full_clean()

    def test_maximum_four_homepage_projects(self):
        for i in range(4):
            Project.objects.create(
                title=f"Projet {i}",
                slug=f"projet-{i}",
                short_description="Description test",
                description="Description complète du projet.",
                is_featured=True,
                show_on_homepage=True,
            )

        fifth_project = Project(
            title="Projet 5",
            slug="projet-5",
            short_description="Description test",
            description="Description complète du projet.",
            is_featured=True,
            show_on_homepage=True,
        )

        with self.assertRaises(ValidationError):
            fifth_project.full_clean()