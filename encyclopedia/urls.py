from django.urls import path
from django.urls import include, re_path
from . import views
from . import util

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pk>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("entry", views.entry, name="entry"),
    path("edit/<str:pk>", views.edit, name="edit")
]
