from django.db import models
from escuelas.models import Escuela
from django.template.defaultfilters import slugify

class Expediente(models.Model):
	escuela = models.OneToOneField(Escuela, on_delete=models.CASCADE)
	acta_ubicacion = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Acta de ubicación de bebedero", null=True, blank=True)
	acta_inicio_construccion = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Acta de inicio de construcción", null=True, blank=True)
	cedula_identificacion = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Cédula de identificación", null=True, blank=True)
	convenio_concertacion = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Convenio de concertación de aplicación de recurso", null=True, blank=True)
	plano_conjunto = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Plano de conjunto", null=True, blank=True)
	distribucion_planta = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Distribución en planta", null=True, blank=True)	
	memoria_calculo_1 = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Memoria de cálculo hidráulico", null=True, blank=True)
	memoria_calculo_2 = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Memoria de cálculo sanitario", null=True, blank=True)
	memoria_calculo_3 = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Memoria de cálculo eléctrico", null=True, blank=True)
	isometrico_instalacion = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Isometricos de instalaciones", null=True, blank=True)
	levantamiento_instalacion = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Levantamiento de instalación", null=True, blank=True)
	acta_funcionamiento = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Acta de Inicio de funcionamiento",  null=True, blank=True)
	acta_entrega = models.FileField(upload_to='expedientes/%Y/%m/%d/', verbose_name="Acta de entrega", null=True, blank=True)
	fotografia_antes_1 = models.ImageField(upload_to='fotografias/%Y/%m/%d/', blank=True, null=True)
	fotografia_antes_2 = models.ImageField(upload_to='fotografias/%Y/%m/%d/', blank=True, null=True)
	fotografia_duarnte_1 = models.ImageField(upload_to='fotografias/%Y/%m/%d/', blank=True, null=True)
	fotografia_durante_2 = models.ImageField(upload_to='fotografias/%Y/%m/%d/', blank=True, null=True)
	fotografia_despues_1 = models.ImageField(upload_to='fotografias/%Y/%m/%d/', blank=True, null=True)
	fotografia_despues_2 = models.ImageField(upload_to='fotografias/%Y/%m/%d/', blank=True, null=True)	
	slug = models.SlugField(max_length=50, blank=True, unique=True)

	def __str__(self):
		return '{}'.format(self.escuela)

	def save(self):
		self.slug = "expediente-" + slugify(self.escuela)
		super(Expediente, self).save()


#class Fotografia(models.Model):
#	descripcion_choices = (
#	("Antes", "Antes"),
#	("Durante", "Durante"),
#	("Despues", "Despues"),
#	)
#	escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
#	fotografia = models.ImageField(upload_to='fotografias/%Y/%m/%d/')
#	descripcion = models.CharField(max_length=10, choices=descripcion_choices)

#	def __str__(self):
#		return '{} {}'.format(self.descripcion, self.escuela)

