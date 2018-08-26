# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tareas(models.Model):
    class Meta:
        verbose_name_plural = "Tareas"
        ordering = ["titulo"]

    titulo = models.CharField(max_length=125, blank=True, null=True, help_text="Escribe el título...")
    fecha_ingreso = models.DateField(default=timezone.now)
    descripcion = models.TextField( blank=True, null=True)
    finalizada = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return self.titulo
