from django.urls import path

from . import views


app_name = "hiking"


urlpatterns = [

    path(
        "",
        views.hiking_list,
        name="list",
    ),

    path(
        "<slug:slug>/",
        views.hiking_detail,
        name="detail",
    ),

]