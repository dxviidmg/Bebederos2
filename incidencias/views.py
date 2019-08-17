from django.shortcuts import render
from django.views.generic.list import ListView
from .models import * 
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

class IncidenciaListView(ListView):
	model = Incidencia
#    template_name = 'products/products.html'
#    paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		context['escuela'] = escuela
		context['incidencias'] = Incidencia.objects.filter(escuela=escuela)
#		print(context['mantenimientos'])
#        print(self.kwargs['slug'])
		return context

class IncidenciaCreateView(CreateView):
	model = Incidencia
	fields = ['descripcion', 'status', 'prioridad', 'evidencia_incidencia']

#	success_message = "¡Creacion exitosa!"

	def get_success_url(self):
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		return reverse('incidencias:incidencia-list', args=(escuela.slug,))

	def form_valid(self, form):
		escuela = Escuela.objects.get(slug=self.kwargs['slug'])
		form.instance.escuela = escuela
		form.instance.autor = self.request.user.first_name + " " + self.request.user.last_name
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(IncidenciaCreateView, self).get_context_data(**kwargs)
		context['escuela'] = Escuela.objects.get(slug=self.kwargs['slug'])
		return context

class IncidenciaUpdateView(UpdateView):
	model = Incidencia
	fields = ['descripcion', 'status', 'prioridad', 'evidencia_incidencia', 'solucion', 'evidencia_solucion']

	def get_success_url(self):
		incidencia = Incidencia.objects.get(pk=self.kwargs['pk'])
		escuela = incidencia.escuela
		return reverse('incidencias:incidencia-list', args=(escuela.slug,))

	def get_context_data(self, **kwargs):
		context = super(IncidenciaUpdateView, self).get_context_data(**kwargs)
		incidencia = Incidencia.objects.get(pk=self.kwargs['pk'])
		context['escuela'] = incidencia.escuela
		return context		