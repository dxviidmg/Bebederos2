from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

class AnalisisCreateView(SuccessMessageMixin, CreateView):
	model = Analisis
#	fields = ['fecha_muestreo', 'no_registro', 'evidencia_visita', 'registro_campo', 'cadena_custodia', 'resultado', 'fecha_resultado', 'comparacion_color_verdadero', 'comparacion_turbiedad', 'comparacion_ph', 'comparacion_conductividad_electrica', 'comparacion_coliformes_fecales', 'comparacion_coliformes_totales', 'comparacion_arsenico', 'comparacion_hierro', 'comparacion_manganeso', 'comparacion_plomo', 'comparacion_floururos', 'comparacion_nitratos', 'comparacion_sulfatos', 'comparacion_dureza_total', 'comparacion_solidos_disueltos', 'color_verdadero', 'turbiedad', 'ph', 'conductividad_electrica',	'coliformes_fecales', 'coliformes_totales','arsenico', 'hierro', 'manganeso', 'plomo', 'floururos', 'nitratos', 'sulfatos', 'dureza_total', 'solidos_disueltos', 'dictamen', 'validacion', 'aboratorio']
	fields = ['fecha_muestreo', 'no_registro', 'evidencia_visita', 'registro_campo', 'cadena_custodia', 'resultado', 'fecha_resultado',  'color_verdadero', 'turbiedad', 'ph', 'conductividad_electrica',	'coliformes_fecales', 'coliformes_totales','arsenico', 'hierro', 'manganeso', 'plomo', 'floururos', 'nitratos', 'sulfatos', 'dureza_total', 'solidos_disueltos', 'dictamen', 'laboratorio']

	success_message = "¡Creacion exitosa exitosa!"


	def get_success_url(self):
		ultimo_analisis = Analisis.objects.latest('pk')
		return reverse('agua:analisis-update', args=(ultimo_analisis.slug,))

	def form_valid(self, form):
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		form.instance.escuela = escuela
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(AnalisisCreateView, self).get_context_data(**kwargs)
		context['escuela'] = Escuela.objects.get(slug=self.kwargs['slug'])
#		plan = Plan.objects.get(slug=self.kwargs['slug'])
#		context['plan'] = plan
		return context

class AnalisisUpdateView(SuccessMessageMixin, UpdateView):
	model = Analisis
#	fields = ['fecha_muestreo', 'no_registro', 'evidencia_visita', 'registro_campo', 'cadena_custodia', 'resultado', 'fecha_resultado', 'comparacion_color_verdadero', 'comparacion_turbiedad', 'comparacion_ph', 'comparacion_conductividad_electrica', 'comparacion_coliformes_fecales', 'comparacion_coliformes_totales', 'comparacion_arsenico',	'comparacion_hierro', 'comparacion_manganeso', 'comparacion_plomo', 'comparacion_floururos', 'comparacion_nitratos', 'comparacion_sulfatos', 'comparacion_dureza_total', 'comparacion_solidos_disueltos', 'color_verdadero', 'turbiedad', 'ph', 'conductividad_electrica',	'coliformes_fecales', 'coliformes_totales','arsenico', 'hierro', 'manganeso', 'plomo', 'floururos', 'nitratos', 'sulfatos', 'dureza_total', 'solidos_disueltos', 'dictamen', 'validacion', 'aboratorio']
	fields = ['fecha_muestreo', 'no_registro', 'evidencia_visita', 'registro_campo', 'cadena_custodia', 'resultado', 'fecha_resultado',  'color_verdadero', 'turbiedad', 'ph', 'conductividad_electrica',	'coliformes_fecales', 'coliformes_totales','arsenico', 'hierro', 'manganeso', 'plomo', 'floururos', 'nitratos', 'sulfatos', 'dureza_total', 'solidos_disueltos', 'dictamen', 'laboratorio']

	success_message = "¡Actualizacion exitosa exitosa!"

	def get_success_url(self):
   		return reverse('agua:analisis-update', args=(self.object.slug,))

	def get_context_data(self, **kwargs):
		context = super(AnalisisUpdateView, self).get_context_data(**kwargs)
		analisis = Analisis.objects.get(slug=self.kwargs['slug'])
		context['escuela'] = analisis.escuela
		return context