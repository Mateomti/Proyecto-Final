from django.db import models
from django.contrib.auth.models import User

class DatosExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    fecha_ingreso = models.DateField(null=True)

    def __str__(self):
        return f'Datos extras del usuario {self.user}'
    