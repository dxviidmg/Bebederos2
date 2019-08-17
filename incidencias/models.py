from django.db import models
#from django.contrib.auth.models import User
from escuelas.models import *
from django.utils import timezone

class Incidencia(models.Model):
	status_choices = (
		("En espera", "En espera"),
		("Atendiendo", "Atendiendo"),
		("Solucionado", "Solucionado"),
		("No aplica", "No aplica"),
	)
	prioridad_choices = (
		("Ninguna", "Ninguna (Es una notificación)"),
		("Baja", "Baja"),
		("Media", "Media"),
		("Alta", "Alta"),
	)
	fase_choices = (
		("Primer análisis de agua", "Primer análisis de agua"),
		("Expediente técnico", "Expediente técnico"),
		("Construcción e instalación de Sistema bebedero", "Construcción e instalación de Sistema bebedero"),
		("Segundo análisis de agua", "Segundo análisis de agua"),
		("Mantenimientos", "Mantenimientos"),
	)

	escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
	autor = models.CharField(max_length=50)
	descripcion = models.TextField(verbose_name="Descripción")
	status = models.CharField(max_length=30, default="En espera", choices=status_choices)
	prioridad = models.CharField(max_length=10, choices=prioridad_choices)
	solucion = models.TextField(verbose_name="Solución", null=True, blank=True)
	fecha_solucion = models.DateTimeField(verbose_name="Fecha de solucion", null=True, blank=True)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	evidencia_incidencia = models.ImageField(upload_to="incidencias/%Y/%m/%d/", null=True, blank=True, verbose_name="Evidencia de incidencia")
	evidencia_solucion = models.ImageField(upload_to="incidencias/%Y/%m/%d/", null=True, blank=True, verbose_name="Evidencia de solución")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['creacion']

	def save(self):
		if self.status == "Solucionado":
			print("hola")
#			print(timezone.now())
			self.fecha_solucion = timezone.now()
			print(self.fecha_solucion)
		super(Incidencia, self).save()