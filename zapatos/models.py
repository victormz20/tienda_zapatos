from django.db import models

class Zapato(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    proveedor = models.CharField(max_length=200)
    precio_total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre