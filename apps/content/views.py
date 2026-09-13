from django.shortcuts import get_object_or_404, render

from .models import Article


# ==========================================================
# PAGE NEWSLETTER
# ==========================================================

def newsletter(request):

    electronic_articles = Article.objects.filter(
        category__slug="electronique",
        is_published=True,
    )[:3]

    hiking_articles = Article.objects.filter(
        category__slug="randonnee",
        is_published=True,
    )[:3]

    context = {
        "electronic_articles": electronic_articles,
        "hiking_articles": hiking_articles,
    }

    return render(
        request,
        "content/newsletter.html",
        context,
    )


# ==========================================================
# DÉTAIL D'UN ARTICLE
# ==========================================================

def article_detail(request, slug):

    article = get_object_or_404(
        Article,
        slug=slug,
        is_published=True,
    )

    return render(
        request,
        "content/article_detail.html",
        {
            "article": article,
        },
    )