from django.urls import path

from . import views


app_name = "content"


urlpatterns = [

    # Newsletter
    path(
        "",
        views.newsletter,
        name="newsletter",
    ),

    # Détail d'un article
    path(
        "<slug:slug>/",
        views.article_detail,
        name="article_detail",
    ),

]