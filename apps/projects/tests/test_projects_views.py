from django.test import TestCase
from django.urls import reverse

from apps.projects.models import Project


class ProjectViewsTests(TestCase):

    def test_project_list_page(self):
        response = self.client.get(reverse("projects:list"))

        self.assertEqual(response.status_code, 200)

    def test_project_list_only_shows_featured_projects(self):
        featured_project = Project.objects.create(
            title="Projet visible",
            slug="projet-visible",
            short_description="Projet visible dans la liste.",
            description="Description du projet visible.",
            is_featured=True,
        )

        hidden_project = Project.objects.create(
            title="Projet masqué",
            slug="projet-masque",
            short_description="Projet masqué de la liste.",
            description="Description du projet masqué.",
            is_featured=False,
        )

        response = self.client.get(reverse("projects:list"))

        self.assertContains(response, featured_project.title)
        self.assertNotContains(response, hidden_project.title)

    def test_project_detail_page(self):
        project = Project.objects.create(
            title="Projet détail",
            slug="projet-detail",
            short_description="Projet de test.",
            description="Description complète du projet.",
            is_featured=True,
        )

        response = self.client.get(
            reverse("projects:detail", kwargs={"slug": project.slug})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, project.title)

    def test_project_detail_unknown_slug_returns_404(self):
        response = self.client.get(
            reverse(
                "projects:detail",
                kwargs={"slug": "projet-inexistant"},
            )
        )

        self.assertEqual(response.status_code, 404)