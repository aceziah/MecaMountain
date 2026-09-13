from django.contrib import admin
from django.template.response import TemplateResponse

from .models import Project


def homepage_order_view(request):
    projects = Project.objects.filter(
        show_on_homepage=True
    ).order_by("homepage_order")

    context = {
        **admin.site.each_context(request),
        "title": "Ordre d'affichage Accueil",
        "projects": projects,
    }

    return TemplateResponse(
        request,
        "admin/projects/homepage_order.html",
        context,
    )