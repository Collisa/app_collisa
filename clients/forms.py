from django.forms import ModelForm, TextInput, EmailInput

from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ("created_at",)
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "kind_of": TextInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "street": TextInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "street_num": TextInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 6,
                    "rows": 1,
                }
            ),
            "postal_code": TextInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 6,
                    "rows": 1,
                }
            ),
            "town": TextInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "vat": TextInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "invoice_email": EmailInput(
                attrs={
                    "class": "border border-teal-400 rounded-lg pl-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
        }


class AllClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ("created_at",)
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "kind_of": TextInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "street": TextInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "street_num": TextInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 6,
                    "rows": 1,
                }
            ),
            "postal_code": TextInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 6,
                    "rows": 1,
                }
            ),
            "town": TextInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "vat": TextInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
            "invoice_email": EmailInput(
                attrs={
                    "class": "border-2 border-teal-400 rounded-lg p-2",
                    "cols": 20,
                    "rows": 1,
                }
            ),
        }
