from django.shortcuts import render
from django.views.generic.list import ListView
from .models import * 
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

class MantenimientoListView(ListView):
	model = Mantenimiento
#    template_name = 'products/products.html'
#    paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		context['escuela'] = escuela
		context['mantenimientos'] = Mantenimiento.objects.filter(escuela=escuela)
#		print(context['mantenimientos'])
#        print(self.kwargs['slug'])
		return context

class MantenimientoCreateView(CreateView):
	model = Mantenimiento
	fields = ['fecha', 'tipo', 'descripcion', 'volumen', 'carnet', 'foto_inicio', 'foto_fin', 'foto_medidor']

#	success_message = "¡Creacion exitosa!"

	def get_success_url(self):
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		return reverse('mantenimientos:mantenimiento-list', args=(escuela.slug,))

	def form_valid(self, form):
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		form.instance.escuela = escuela
		return super().form_valid(form)

class MantenimientoUpdateView(UpdateView):
	model = Mantenimiento
	fields = ['fecha', 'tipo', 'descripcion', 'volumen', 'carnet', 'foto_inicio', 'foto_fin', 'foto_medidor']

	success_message = "¡Actualizacion exitosa exitosa!"

	def get_success_url(self):
#		print(self.kwargs['pk'])
		mantenimiento = Mantenimiento.objects.get(pk=self.kwargs['pk'])
		escuela = mantenimiento.escuela
#		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		return reverse('mantenimientos:mantenimiento-list', args=(escuela.slug,))	