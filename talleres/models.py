from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

class Taller(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]

    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    duracion_horas = models.FloatField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    observacion = models.TextField(null=True, blank=True)

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    propuesto_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"
