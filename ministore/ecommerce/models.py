from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ("GM", "GYM"),
    ("LB", "LIBROS"),
]

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_link = models.URLField(null=True)
    categoria = models.CharField(max_length=2,choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.nombre
    
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.usuario.username
