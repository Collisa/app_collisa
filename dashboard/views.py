from django.shortcuts import render


def dashboard(request):
    context = {"dashboard": True}
    return render(request, "dashboard/index.html", context)
