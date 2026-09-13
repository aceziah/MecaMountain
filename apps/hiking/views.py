from django.shortcuts import get_object_or_404, render

from .models import Hiking


def hiking_list(request):

    hikings = Hiking.objects.filter(
        is_published=True
    ).order_by("-date")

    context = {
        "hikings": hikings,
    }

    return render(
        request,
        "hiking/hiking_list.html",
        context,
    )


def hiking_detail(request, slug):

    hiking = get_object_or_404(
        Hiking,
        slug=slug,
        is_published=True,
    )

    context = {
        "hiking": hiking,
    }

    return render(
        request,
        "hiking/hiking_detail.html",
        context,
    )