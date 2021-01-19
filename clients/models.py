from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    kind_of = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_num = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    vat = models.CharField(max_length=25, null=True, blank=True)
    invoice_email = models.EmailField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="contact"
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.client}"


class Order(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="order")
    description = models.CharField(max_length=50)
    todo = models.TextField()
    work_hours = models.DurationField()
    estimated_price = models.DecimalField(max_digits=20, decimal_places=2)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.description}; {self.client}"
