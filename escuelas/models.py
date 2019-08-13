from django.db import models
from django.template.defaultfilters import slugify

nivel_choices = (
	("Preescolar", "Preescolar"),
	("Primaria", "Primaria"),
	("Secundaria", "Secundaria"),
)

turno_choices = (
	("Matutino", "Matutino"),
	("Vespertino", "Vespertino"),
	("Tiempo Completo", "Tiempo Completo"),
)

class Region(models.Model):
	numero = models.IntegerField()
	nombre = models.CharField(max_length=20)
	slug = models.SlugField(max_length=50, blank=True, unique=True)

	def __str__(self):
		return '{} {}'.format(self.numero, self.nombre)

	def save(self):
		self.slug = '-'.join((slugify(self.numero), slugify(self.nombre)))
		super(Region, self).save()

class Convocatoria(models.Model):
	año = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.año)

class Entidad(models.Model):
	region = models.ForeignKey(Region, verbose_name="Región", on_delete=models.CASCADE)
	partida = models.IntegerField()
	nombre = models.CharField(max_length=20)
	abreviatura	= models.CharField(max_length=4)
	slug = models.SlugField(max_length=50, blank=True, unique=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.slug= slugify(self.nombre)
		super(Entidad, self).save()

class EntidadConvocatoria(models.Model):
	entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
	convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE)
	escuelas_contractuadas = models.IntegerField()
	escuelas_registradas = models.IntegerField(default=0)
	escuelas_sustituidas = models.IntegerField(default=0)
	slug = models.SlugField(max_length=50, blank=True, unique=True)

	def __str__(self):
		return '{} {}'.format(self.entidad, self.convocatoria)

	def save(self):
		self.slug = '-'.join((slugify(self.entidad), slugify(self.convocatoria)))
		super(EntidadConvocatoria, self).save()

class Escuela(models.Model):
	#Convocatoria
	entidad_convocatoria = models.ForeignKey(EntidadConvocatoria, on_delete=models.CASCADE)
	numero = models.IntegerField()
	#Administrativos
	cct = models.CharField(max_length=10)
	nombre = models.TextField()
	nivel_educativo = models.CharField(max_length=20, choices=nivel_choices)
	turno = models.CharField(max_length=20, default="Matutino", choices=turno_choices)
	plantilla_escolar = models.IntegerField()
	#Ubicacion
	municipio = models.CharField(max_length=50)
	domicilio = models.TextField()
	localidad = models.CharField(max_length=50)
	#Contacto
	director = models.CharField(max_length=50, blank=True, null=True)
	telefono = models.CharField(max_length=10, blank=True, null=True)
	esta_sustituida = models.BooleanField(default=False)
	es_sustitucion = models.BooleanField(default=False)
#	avance = models.IntegerField(blank=True, null=True)
#	evidencias = models.IntegerField(null=True, blank=True)
#	mantenimientos = models.IntegerField(null=True, blank=True)

	slug = models.SlugField(max_length=50, blank=True, unique=True)

	def save(self):
		self.slug = '-'.join((slugify(self.cct), slugify(self.nombre)))
		super(Escuela, self).save()

	def __str__(self):
		return '{} {}'.format(self.cct, self.nombre)		