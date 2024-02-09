from django.db import models


class Credenciales(models.Model):
    rut = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.rut
