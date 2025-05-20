from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    # path("", views.index, name="index"),
    path("pages/about/", views.about, name="about"),
    path("pages/rules/", views.rules, name="rules"),
]
