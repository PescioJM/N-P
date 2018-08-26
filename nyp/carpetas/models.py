# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User

class Productores(models.Model):

    class Meta:
        verbose_name_plural = "Productores"
#        ordering = ["razon_social"]
#    razon_social = models.ForeignKey(User, null=True, default=True)
#    oficinas =
    responsable = models.CharField(max_length=255, blank=True, null=True,
    help_text=('Ingrese el nombre del contacto responsable de llevar el caso por parte de la empresa'))
    fecha_de_ingreso = models.DateField(default=timezone.now)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    codigo_postal = models.CharField(max_length=25, blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
'''
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return self.razon_social
PENDIENTE GENERAR QUE IMPRIMA LA RAZON SOCIAL. ADEMAS OPCION AGREGAR OFICINAS.
PENSAR QUIZA QUE GROUPS puede ser el PRODUCTOR y USER las oficinas !!!!!
'''
class Gestion(models.Model):
    class Meta:
        verbose_name_plural = "Gestion"
        ordering = ["apellido_y_nombre"]
    productor = models.ForeignKey(Productores, null = True, blank = True, on_delete=models.CASCADE)
    apellido_y_nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion_general = models.TextField(max_length=255, blank=True, null=True)
    compania_asegurado = models.CharField(max_length=50, blank=True, null=True)
    compania_tercero = models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso = models.DateField(default=timezone.now)
    liquidacion_del_cliente = models.BooleanField(default=False)
    finalizada = models.BooleanField(default=False)
    media = models.FileField(upload_to='Mi Carpeta/', blank=True, null=True, help_text='Adjuntar archivo')

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return self.apellido_y_nombre
