from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

class ExpedienteCreateView(SuccessMessageMixin, CreateView):
	model = Expediente
	fields = [	'acta_ubicacion', 'acta_inicio_construccion', 'cedula_identificacion', 'convenio_concertacion', 'plano_conjunto', 'distribucion_planta', 'memoria_calculo_1', 'memoria_calculo_2', 'memoria_calculo_3', 'isometrico_instalacion', 'levantamiento_instalacion', 'acta_funcionamiento', 'acta_entrega',]

	success_message = "¡Creacion exitosa!"

	def get_success_url(self):
		ultimo_expediente = Expediente.objects.latest('pk')
		return reverse('expedientes:expediente-update', args=(ultimo_expediente.slug,))

	def form_valid(self, form):
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		form.instance.escuela = escuela
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ExpedienteCreateView, self).get_context_data(**kwargs)
		context['escuela'] = Escuela.objects.get(slug=self.kwargs['slug'])
#		plan = Plan.objects.get(slug=self.kwargs['slug'])
#		context['plan'] = plan
		return context

class ExpedienteUpdateView(SuccessMessageMixin, UpdateView):
	model = Expediente
	fields = ['acta_ubicacion', 'acta_inicio_construccion', 'cedula_identificacion', 'convenio_concertacion', 'plano_conjunto', 'distribucion_planta', 'memoria_calculo_1', 'memoria_calculo_2', 'memoria_calculo_3', 'isometrico_instalacion', 'levantamiento_instalacion', 'acta_funcionamiento', 'acta_entrega',]

	success_message = "¡Actualizacion exitosa exitosa!"

	def get_success_url(self):
		return reverse('expedientes:expediente-update', args=(self.object.slug,))

	def get_context_data(self, **kwargs):
		context = super(ExpedienteUpdateView, self).get_context_data(**kwargs)
		expediente = Expediente.objects.get(slug=self.kwargs['slug'])
		context['escuela'] = expediente.escuela
		return context
