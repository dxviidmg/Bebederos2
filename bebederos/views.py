from django.shortcuts import render
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

class SistemaBebederoUpdateView(SuccessMessageMixin, UpdateView):
	model = SistemaBebedero
	fields = ['mueble', 'sistema_potabilizador', 'num_serie_mueble', 'esta_en_campo']
	success_message = "¡Actualizacion exitosa exitosa!"

	def get_success_url(self):
		return reverse('bebederos:sistemabebedero-update',args=(self.object.slug,))

	def get_context_data(self, **kwargs):
		context = super(SistemaBebederoUpdateView, self).get_context_data(**kwargs)
		sistemabebedero = SistemaBebedero.objects.get(slug=self.kwargs['slug'])
		context['escuela'] = sistemabebedero.escuela
#		plan = Plan.objects.get(slug=self.kwargs['slug'])
#		context['plan'] = plan
		return context		