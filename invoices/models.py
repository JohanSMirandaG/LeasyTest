from django.db import models
from contracts.models import Contract

class Invoice(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="invoices")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    installment_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Factura {self.installment_number} - {self.contract.client}"