from django.urls import path

from . import views


urlpatterns = [
    path("", views.clients, name="clients"),
    path("add_client", views.add_client, name="add_client"),
    path("<id>/", views.client_detail, name="client_detail"),
    path("<id>/change/", views.change_client, name="change_client"),
]
