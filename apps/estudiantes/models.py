from django.db import models

from apps.common.constants import ESTUDIANTE_TIPO_CHOICES


class ORMEstudiante(models.Model):

    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=ESTUDIANTE_TIPO_CHOICES)
