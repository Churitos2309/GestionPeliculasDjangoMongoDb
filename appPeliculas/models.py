# from django.db import models
from djongo import models


class Genero(models.Model):
    _id = models.ObjectIdField()
    genNombre = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.genNombre


class Pelicula(models.Model):
    _id = models.ObjectIdField()
    pelCodigo = models.CharField(max_length=15)
    pelTitulo = models.CharField(max_length=50)
    pelProtagonista = models.CharField(max_length=50)
    pelDuracion = models.IntegerField()
    pelResumen = models.CharField(max_length=1000)
    pelFoto = models.ImageField(upload_to=f"fotos/", null=True, blank=True)
    pelGenero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.pelTitulo
