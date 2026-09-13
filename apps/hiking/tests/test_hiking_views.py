from datetime import date

from django.test import TestCase
from django.urls import reverse

from apps.hiking.models import Hiking


class HikingViewsTests(TestCase):

    def test_hiking_list_page(self):
        response = self.client.get(reverse("hiking:list"))

        self.assertEqual(response.status_code, 200)

    def test_hiking_list_only_shows_published_hikings(self):
        published_hiking = Hiking.objects.create(
            title="Randonnée publiée",
            slug="randonnee-publiee",
            location="Chalmazel",
            massif="Monts du Forez",
            date=date(2026, 8, 15),
            short_description="Une randonnée publiée.",
            description="Description de la randonnée publiée.",
            is_published=True,
        )

        hidden_hiking = Hiking.objects.create(
            title="Randonnée masquée",
            slug="randonnee-masquee",
            location="Chalmazel",
            massif="Monts du Forez",
            date=date(2026, 8, 10),
            short_description="Une randonnée masquée.",
            description="Description de la randonnée masquée.",
            is_published=False,
        )

        response = self.client.get(reverse("hiking:list"))

        self.assertContains(response, published_hiking.title)
        self.assertNotContains(response, hidden_hiking.title)

    def test_hiking_detail_page(self):
        hiking = Hiking.objects.create(
            title="Randonnée détail",
            slug="randonnee-detail",
            location="Chalmazel",
            massif="Monts du Forez",
            date=date(2026, 8, 20),
            short_description="Randonnée de test.",
            description="Description complète de la randonnée.",
            is_published=True,
        )

        response = self.client.get(
            reverse(
                "hiking:detail",
                kwargs={"slug": hiking.slug},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, hiking.title)

    def test_hiking_detail_unknown_slug_returns_404(self):
        response = self.client.get(
            reverse(
                "hiking:detail",
                kwargs={"slug": "randonnee-inexistante"},
            )
        )

        self.assertEqual(response.status_code, 404)