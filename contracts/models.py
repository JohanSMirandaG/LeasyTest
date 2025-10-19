from django.db import models
from clients.models import Client
from cars.models import Car

class Contract(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    weekly_amount = models.DecimalField(max_digits=10, decimal_places=2)
    weeks = models.PositiveIntegerField()
    start_date = models.DateField()

    def __str__(self):
        return f"Contrato {self.id} - {self.client}"