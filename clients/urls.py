from django.urls import path

from . import views


urlpatterns = [
    path("", views.clients, name="clients"),
    path("add_client", views.add_client, name="add_client"),
    path("<id>/", views.client_detail, name="client_detail"),
    path("<id>/change/", views.change_client, name="change_client"),
    path(
        "<id>/chang_client_detail/",
        views.change_client_detail,
        name="change_client_detail",
    ),
    path("<id>/add_contact/", views.add_contact, name="add_contact"),
    path("<id>/add_order/", views.add_order, name="add_order"),
]
