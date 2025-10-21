from django.db import models
from clients.models import Client
from cars.models import Car

class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    weekly_amount = models.DecimalField(max_digits=10, decimal_places=2)
    weeks = models.PositiveIntegerField(default=52)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contrato {self.id} - {self.client}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["client"],
                condition=models.Q(is_active=True),
                name="unique_active_contract_per_client"
            ),
            models.UniqueConstraint(
                fields=["car"],
                condition=models.Q(is_active=True),
                name="unique_active_contract_per_car"
            ),
        ]
        ordering = ["created_at"]