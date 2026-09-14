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

    def test_homepage_projects_follow_manual_order(self):
        project_1 = Project.objects.create(
            title="Projet 1",
            slug="projet-1",
            short_description="Projet 1",
            description="Description du projet 1",
            is_featured=True,
            show_on_homepage=True,
            homepage_order=3,
        )

        project_2 = Project.objects.create(
            title="Projet 2",
            slug="projet-2",
            short_description="Projet 2",
            description="Description du projet 2",
            is_featured=True,
            show_on_homepage=True,
            homepage_order=1,
        )

        project_3 = Project.objects.create(
            title="Projet 3",
            slug="projet-3",
            short_description="Projet 3",
            description="Description du projet 3",
            is_featured=True,
            show_on_homepage=True,
            homepage_order=2,
        )

        response = self.client.get(reverse("core:home"))

        projects = list(response.context["featured_projects"])

        self.assertEqual(
            projects,
            [project_2, project_3, project_1],
        )

    def test_project_list_follows_manual_order(self):
        project_1 = Project.objects.create(
            title="Projet 1",
            slug="projet-1",
            short_description="Projet 1",
            description="Description du projet 1",
            is_featured=True,
            project_order=3,
        )

        project_2 = Project.objects.create(
            title="Projet 2",
            slug="projet-2",
            short_description="Projet 2",
            description="Description du projet 2",
            is_featured=True,
            project_order=1,
        )

        project_3 = Project.objects.create(
            title="Projet 3",
            slug="projet-3",
            short_description="Projet 3",
            description="Description du projet 3",
            is_featured=True,
            project_order=2,
        )

        response = self.client.get(reverse("projects:list"))

        projects = list(response.context["projects"])

        self.assertEqual(
            projects,
            [project_2, project_3, project_1],
        )