from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage

from apps.projects.models import Project

from .forms import ContactForm


def home(request):

    featured_projects = Project.objects.filter(
        is_featured=True,
        show_on_homepage=True,
    ).order_by("homepage_order")[:4]

    context = {
        "featured_projects": featured_projects,
    }

    return render(
        request,
        "core/home.html",
        context,
    )

def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            email_message = EmailMessage(
                subject=f"[MecaMountain] {subject}",
                body=(
                    f"Nom : {name}\n"
                    f"Email : {email}\n\n"
                    f"Message :\n"
                    f"{message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )

            email_message.send()

            return render(
                request,
                "core/contact.html",
                {
                    "form": ContactForm(),
                    "success": True,
                },
            )

    else:

        form = ContactForm()

    return render(
        request,
        "core/contact.html",
        {
            "form": form,
        },
    )


def privacy(request):

    return render(
        request,
        "core/privacy.html",
    )