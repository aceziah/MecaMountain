from django.shortcuts import get_object_or_404, render

from .models import Project


def project_list(request):

    projects = Project.objects.filter(
        is_featured=True
    )

    context = {
        "projects": projects,
    }

    return render(
        request,
        "projects/project_list.html",
        context,
    )


def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
    )

    context = {
        "project": project,
    }

    return render(
        request,
        "projects/project_detail.html",
        context,
    )