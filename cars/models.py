from django.db import models

class Car(models.Model):
    plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    fabrication_date = models.DateField()

    def __str__(self):
        return f"{self.plate} - {self.brand} {self.model}"