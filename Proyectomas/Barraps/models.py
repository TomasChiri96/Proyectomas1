from django.db import models

# Create your models here.
class mesas(models.Model):
    nro_mesa = models.IntegerField("numero mesa")
    mesa_libre = models.BooleanField()

class mozo(models.Model):
    nombre = models.CharField("nombre", max_length=20)
    apellido = models.CharField("apellido", max_length=20)
    numero = models.IntegerField("numero")

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}, {self.numero}"

class almancen(models.Model):
    producto = models.CharField("producto", max_length=20)
    stock = models.BooleanField("stock")


