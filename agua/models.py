from django.db import models
from escuelas.models import Escuela
from django.utils import timezone
from django.template.defaultfilters import slugify

validacion_choices = (
	("Validado", "Validado"),
	("No validado", "No validado"),
	("En espera", "En espera"),
)

comparacion_choices = (
	("=", "="),
	("<", "<"),
	("≥", "≥"),
	("≤", "≤"),
)

class Dictamen(models.Model):
	nombre = models.CharField(max_length=15)
	fecha = models.DateField(default=timezone.now)
	documento = models.FileField(upload_to='dictamenes/%Y/%m/%d/')

	def __str__(self):
		return '{}'.format(self.nombre)

class Analisis(models.Model):
	escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
	numero = models.IntegerField(blank=True)

	fecha_muestreo = models.DateField(default=timezone.now, verbose_name="Fecha de muestreo")
	no_registro = models.CharField(max_length=30, null=True, blank=True, verbose_name="Número de registro (Orden de Trabajo)")
	evidencia_visita = models.FileField(upload_to='evidencia_visita/%Y/%m/%d/', verbose_name="Evidencia de visita", null=True, blank=True)
	registro_campo = models.FileField(upload_to='registros_campo/%Y/%m/%d/', verbose_name="Registro de campo", null=True, blank=True)
	cadena_custodia = models.FileField(upload_to='cadenas_custioda/%Y/%m/%d/', verbose_name="Cadena de custodia", null=True, blank=True)
	resultado = models.FileField(upload_to='resultados/%Y/%m/%d/', verbose_name="Resultados de análisis de laboratorio", null=True, blank=True)
	fecha_resultado = models.DateField(null=True, blank=True, verbose_name="Fecha del resultado de análisis")

	#Comparaciones
	comparacion_color_verdadero = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_turbiedad = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_ph = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_conductividad_electrica = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_coliformes_fecales = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_coliformes_totales  = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_arsenico = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_hierro = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_manganeso  = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_plomo = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_floururos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_nitratos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_sulfatos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_dureza_total = models.CharField(max_length=1, choices=comparacion_choices, default="=",verbose_name=".")
	comparacion_solidos_disueltos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")

	#Parametros
		#Fisicos y organoelectricos
	color_verdadero = models.FloatField(null=True, blank=True, verbose_name="Color verdadero (U Pt-Co)")
	turbiedad = models.FloatField(null=True, blank=True, verbose_name="Turbiedad (UTN o equivalente)")
	ph = models.FloatField(null=True, blank=True, verbose_name="pH (unidades de pH)")
	conductividad_electrica = models.FloatField(null=True, blank=True, verbose_name="Conductividad eléctrica (µS/cm)")
		#Bacteriologicos
	coliformes_fecales = models.FloatField(null=True, blank=True, verbose_name="Coliformes fecales (UFC o NMP)")
	coliformes_totales = models.FloatField(null=True, blank=True, verbose_name="Coliformes totales (UFC o NMP)") 
		#Arsenico y metales
	arsenico = models.FloatField(null=True, blank=True, verbose_name="Arsénico (mg/L)")
	hierro = models.FloatField(null=True, blank=True, verbose_name="Hierro (mg/L)")
	manganeso = models.FloatField(null=True, blank=True, verbose_name="Manganeso (mg/L)")
	plomo = models.FloatField(null=True, blank=True, verbose_name="Plomo (mg/L)")
		#Iones y compuestos inorganicos
	floururos = models.FloatField(null=True, blank=True, verbose_name="Fluoruros (mg/L)")
	nitratos = models.FloatField(null=True, blank=True, verbose_name="Nitratos (mg/L)")
	sulfatos = models.FloatField(null=True, blank=True, verbose_name="Sulfatos (mg/L)")
	dureza_total = models.FloatField(null=True, blank=True, verbose_name="Dureza total (CaCO3) (mg/L)")
	solidos_disueltos  = models.FloatField(null=True, blank=True, verbose_name="Sólidos disueltos totales (mg/L)")	

	#Fase de confirmación / ECA
	dictamen = models.ForeignKey(Dictamen, null=True, blank=True, on_delete=models.CASCADE)
	validacion = models.BooleanField(default=False)
	aboratorio = models.CharField(max_length=30, null=True, blank=True)
	slug = models.SlugField(max_length=50, blank=True, unique=True)

	def __str__(self):
		return '{} {}'.format(self.numero, self.escuela)	

	def save(self):
		if not self.pk:
			analisis = Analisis.objects.filter(escuela=self.escuela).count()
			self.numero = analisis + 1
			self.slug = "analisis-" + '-'.join((slugify(self.numero), slugify(self.escuela)))
		if self.dictamen:
			self.validacion = True	
		super(Analisis, self).save()