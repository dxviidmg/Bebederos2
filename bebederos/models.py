from django.db import models
from escuelas.models import Escuela
from django.template.defaultfilters import slugify

nivel_choices = (
	("Preescolar", "Preescolar"),
	("Primaria", "Primaria"),
	("Secundaria", "Secundaria"),
)

rango_choices = (
("1-300", "1-300"),
("301-400", "301-400"),
("401-600", "401-600"),
("601 o más", "601 o más"),	
)

#class Proveedor(models.Model):
#	nombre = models.CharField(max_length=20)	

#	def __str__(self):
#		return '{}'.format(self.nombre)

class SistemaPotabilizador(models.Model):
	tipo = models.CharField(max_length=20)
#	ficha_tecnica = models.FileField(upload_to='ficha_tecnica/%Y/%m/%d/', verbose_name="Ficha técnica", null=True, blank=True)
#	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.tipo,)

class Mueble(models.Model):
	modelo = models.CharField(max_length=20, null=True, blank=True)
	nivel_educativo = models.CharField(max_length=20, choices=nivel_choices)
	rango = models.CharField(max_length=10, choices=rango_choices)
#	ficha_tecnica = models.FileField(upload_to='ficha_tecnica/%Y/%m/%d/', verbose_name="Ficha técnica", null=True, blank=True)
#	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)	

	def __str__(self):
		return '{}'.format(self.modelo)

	def save(self):
		if self.nivel_educativo == "Preescolar":
			modelo = "PE"
		elif self.nivel_educativo == "Primaria":
			modelo = "PI"
		else:
			modelo = "SC"

		if self.rango == "1-300":
			modelo = modelo + "-01"
		elif self.rango == "301-400":
			modelo = modelo + "-02"
		elif self.rango == "401-600":
			modelo = modelo + "-03"		
		else:
			modelo = modelo + "-04"

		self.modelo = modelo
		super(Mueble, self).save()

class SistemaBebedero(models.Model):
	escuela = models.OneToOneField(Escuela, on_delete=models.CASCADE, related_name="escuela_sistemabebedero")
	mueble = models.ForeignKey(Mueble, on_delete=models.CASCADE)
	sistema_potabilizador = models.ForeignKey(SistemaPotabilizador, on_delete=models.CASCADE, blank=True, null=True)
	num_serie_mueble = models.CharField(max_length=20, null=True, blank=True)
	no_trazabilidad = models.TextField(null=True, blank=True)
	esta_en_campo = models.BooleanField(default=False)
	slug = models.SlugField(max_length=50, blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.escuela)

	def save(self):
		self.slug = "sb-" + slugify(self.escuela)
		if self.sistema_potabilizador and self.num_serie_mueble:
			self.no_trazabilidad = '-'.join((slugify(self.escuela.entidad_convocatoria.entidad.abreviatura), slugify(self.escuela.cct), slugify(self.mueble), slugify("nsm"), slugify(self.num_serie_mueble))).upper()
		super(SistemaBebedero, self).save()