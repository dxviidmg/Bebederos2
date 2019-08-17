from django.urls import path
from .views import *

app_name = 'incidencias'

urlpatterns = [
	path('incidencia/update/<int:pk>/', IncidenciaUpdateView.as_view(), name='incidencia-update'),
	path('nueva-incidencia/escuela/<slug:slug>/', IncidenciaCreateView.as_view(), name='incidencia-create'),
	path('escuela/<slug:slug>/incidencias-y-notas/', IncidenciaListView.as_view(), name='incidencia-list'),
]