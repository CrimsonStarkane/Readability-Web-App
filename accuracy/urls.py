from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts", views.contacts, name="contacts"),
    path("<str:formula>", views.prompt, name="prompt"),
    path("<str:formula>/texts", views.texts, name="texts")
]