from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings 

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    # Campos adicionales opcionales
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class Fundacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    disponible = models.BooleanField(default=True)
    fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Adopcion(models.Model):
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # <-- cambia aquí
    fundacion = models.ForeignKey('Fundacion', on_delete=models.CASCADE)
    fecha_adopcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} adoptó {self.mascota.nombre}"
