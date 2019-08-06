from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class RegionListView(ListView):
	model = Region

class RegionDetailView(DetailView):
	model = Region

	def get_context_data(self, **kwargs):
		context = super(RegionDetailView, self).get_context_data(**kwargs)
		context['entidades'] = Entidad.objects.filter(region=self.object)
#		print(context['entidades'])
#		print(self.object)
		return context

class EntidadDetailView(DetailView):
	model = Entidad

	def get_context_data(self, **kwargs):
		context = super(EntidadDetailView, self).get_context_data(**kwargs)
		context['entidad_convocatorias'] = EntidadConvocatoria.objects.filter(entidad=self.object)
#		print(context['entidades'])
#		print(self.object)
		return context

class EntidadConvocatoriaDetailView(DetailView):
	model = EntidadConvocatoria

	def get_context_data(self, **kwargs):
		context = super(EntidadConvocatoriaDetailView, self).get_context_data(**kwargs)
		context['escuelas'] = Escuela.objects.filter(entidad_convocatoria=self.object)
#		print(context['entidades'])
#		print(self.object)
		return context	

class EscuelaDetailView(DetailView):
	model = Escuela

#	def get_context_data(self, **kwargs):
#		context = super(EntidadConvocatoriaDetailView, self).get_context_data(**kwargs)
#		context['escuelas'] = Escuela.objects.filter(entidad_convocatoria=self.object)
#		print(context['entidades'])
#		print(self.object)
#		return context		