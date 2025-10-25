from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    precio=models.FloatField()

    def __str__(self):
        return f"{self.descripcion} - ${self.precio}"