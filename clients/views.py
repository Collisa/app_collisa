from django.shortcuts import render, redirect

from .models import Client, Contact, Order
from .forms import ClientForm, AllClientForm


def clients(request):
    client = True
    all_clients = Client.objects.all()
    context = {"client": client, "clients": all_clients}
    return render(request, "clients/index.html", context=context)


def client_detail(request, id):
    client = True
    all_clients = Client.objects.all()
    detail_client = Client.objects.get(id=id)
    contacts = Contact.objects.filter(client__id=detail_client.id)
    orders = Order.objects.filter(client__id=detail_client.id)
    form = ClientForm(instance=detail_client)
    context = {
        "clients": all_clients,
        "client": client,
        "detail_client": detail_client,
        "contacts": contacts,
        "orders": orders,
        "form": form,
    }
    return render(request, "clients/client_detail.html", context=context)


def add_client(request):
    client = True
    form = AllClientForm()
    all_clients = Client.objects.all()
    new_client = None
    if request.method == "POST":
        submitted_form = AllClientForm(request.POST)
        new_client = submitted_form.save()

    context = {
        "form": form,
        "clients": all_clients,
        "new_client": new_client,
        "client": client,
    }
    return render(request, "clients/add_client.html", context=context)


def change_client(request, id):
    client = True
    detail_client = Client.objects.get(id=id)
    form = ClientForm(request.POST, instance=detail_client)
    form.save()
    return redirect("client_detail", detail_client.id)


def change_client_detail(request, id):
    client = True
    context = {"client": client}
    return render(request, "clients/change_client_detail.html", context=context)


# contact pages


def add_contact(request, id):
    client = True
    context = {"client": client}
    return render(request, "clients/add_contact.html", context=context)


def add_order(request, id):
    client = True
    context = {"client": client}
    return render(request, "clients/add_order.html", context=context)
