from django.db import models


class Klant(models.Model):
    firma_naam = models.CharField(max_length=50)
    soort_bedrijf = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    btw_nummer = models.CharField(max_length=25)
    factuur_email = models.EmailField(max_length=50)
    sinds = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Klanten"

    def __str__(self):
        return f"{self.firma_naam}"


class Contact(models.Model):
    klant = models.ForeignKey("Klant", on_delete=models.CASCADE, related_name="contact")
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Contacten"

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}, {self.klant}"
