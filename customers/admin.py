from django.contrib import admin

from .models import Contact, Klant


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 2


class ContactAdmin(admin.ModelAdmin):
    search_fields = ["voornaam", "achternaam", "klant__firma_naam"]
    list_display = ("voornaam", "achternaam", "klant")


class KlantAdmin(admin.ModelAdmin):
    search_fields = ["firma_naam", "soort_bedrijf"]
    list_display = ("firma_naam", "soort_bedrijf", "sinds")
    inlines = [ContactInline]


admin.site.register(Klant, KlantAdmin)
admin.site.register(Contact, ContactAdmin)
