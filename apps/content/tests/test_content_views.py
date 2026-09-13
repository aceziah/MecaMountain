from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.content.models import Article, Category


class ContentViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.electronic_category = Category.objects.create(
            name="Électronique",
            slug="electronique",
            description="Articles autour de l'électronique.",
        )

        cls.hiking_category = Category.objects.create(
            name="Randonnée",
            slug="randonnee",
            description="Articles autour de la randonnée.",
        )

    def test_newsletter_page(self):
        response = self.client.get(
            reverse("content:newsletter")
        )

        self.assertEqual(response.status_code, 200)

    def test_newsletter_only_shows_published_articles(self):
        published_article = Article.objects.create(
            title="Article électronique publié",
            slug="article-electronique-publie",
            category=self.electronic_category,
            short_description="Article publié.",
            content="Contenu de l'article publié.",
            published_at=timezone.now(),
            is_published=True,
        )

        hidden_article = Article.objects.create(
            title="Article électronique masqué",
            slug="article-electronique-masque",
            category=self.electronic_category,
            short_description="Article masqué.",
            content="Contenu de l'article masqué.",
            published_at=timezone.now(),
            is_published=False,
        )

        response = self.client.get(
            reverse("content:newsletter")
        )

        self.assertContains(
            response,
            published_article.title,
        )

        self.assertNotContains(
            response,
            hidden_article.title,
        )

    def test_newsletter_separates_articles_by_category(self):
        electronic_article = Article.objects.create(
            title="Article électronique",
            slug="article-electronique",
            category=self.electronic_category,
            short_description="Article électronique.",
            content="Contenu électronique.",
            published_at=timezone.now(),
            is_published=True,
        )

        hiking_article = Article.objects.create(
            title="Article randonnée",
            slug="article-randonnee",
            category=self.hiking_category,
            short_description="Article randonnée.",
            content="Contenu randonnée.",
            published_at=timezone.now(),
            is_published=True,
        )

        response = self.client.get(
            reverse("content:newsletter")
        )

        self.assertContains(
            response,
            electronic_article.title,
        )

        self.assertContains(
            response,
            hiking_article.title,
        )

    def test_article_detail_page(self):
        article = Article.objects.create(
            title="Article détail",
            slug="article-detail",
            category=self.electronic_category,
            short_description="Article de test.",
            content="Contenu complet de l'article.",
            published_at=timezone.now(),
            is_published=True,
        )

        response = self.client.get(
            reverse(
                "content:article_detail",
                kwargs={"slug": article.slug},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)
        self.assertContains(
            response,
            "Contenu complet de l'article.",
            html=True,
        )

    def test_unpublished_article_detail_returns_404(self):
        article = Article.objects.create(
            title="Article non publié",
            slug="article-non-publie",
            category=self.electronic_category,
            short_description="Article non publié.",
            content="Contenu non publié.",
            published_at=timezone.now(),
            is_published=False,
        )

        response = self.client.get(
            reverse(
                "content:article_detail",
                kwargs={"slug": article.slug},
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_unknown_article_detail_returns_404(self):
        response = self.client.get(
            reverse(
                "content:article_detail",
                kwargs={"slug": "article-inexistant"},
            )
        )

        self.assertEqual(response.status_code, 404)