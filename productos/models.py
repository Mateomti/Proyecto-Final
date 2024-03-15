from django.db import models

class Productos(models.Model):
    marca = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField()
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.marca} - {self.nombre}'
