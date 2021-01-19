from django.contrib import admin

from .models import Contact, Client, Order


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1


class OrderInline(admin.StackedInline):
    model = Order
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    search_fields = ["first_name", "last_name", "client__name"]
    list_display = ("first_name", "last_name", "client")


class ClientAdmin(admin.ModelAdmin):
    search_fields = ["name", "kind_of"]
    list_display = ("name", "kind_of", "created_at")
    inlines = [ContactInline, OrderInline]


class OrderAdmin(admin.ModelAdmin):
    list_display = ("client", "work_hours", "estimated_price")


admin.site.register(Client, ClientAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Order, OrderAdmin)
