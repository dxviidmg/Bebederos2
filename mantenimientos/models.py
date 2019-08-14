from django.db import models
from escuelas.models import Escuela
from django.utils import timezone

class Mantenimiento (models.Model):
	tipo_choices =  (
		('Preventivo' , 'Preventivo'),
		('Correctivo' , 'Correctivo'),
	)

	escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	fecha = models.DateField(default=timezone.now, verbose_name="Fecha de mantenimiento")
	tipo = models.CharField(max_length=20, default="Preventivo", choices=tipo_choices)
	descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
	volumen = models.IntegerField(verbose_name="Volumen indicado en medidor (Litros)")
			
	carnet = models.ImageField(verbose_name="Carnet actualizado", upload_to='mantenimientos/%Y/%m/%d/')
	foto_inicio = models.ImageField(verbose_name="Foto al iniciar el mantenimiento", upload_to='mantenimientos/%Y/%m/%d/')
	foto_fin = models.FileField(verbose_name="Foto al finalizar el mantenimiento", upload_to='mantenimientos/%Y/%m/%d/')
	foto_medidor = models.FileField(verbose_name="Foto del medidor", upload_to='mantenimientos/%Y/%m/%d/', null=True, blank=True)

	def __str__(self):
		return '{} {}'.format(self.escuela, self.fecha)