from django.urls import path
from .views import *

app_name = 'expedientes'

urlpatterns = [
	path('nuevo-expediente/escuela/<slug:slug>/', ExpedienteCreateView.as_view(), name='expediente-create'),
	path('update-expediente/<slug:slug>/', ExpedienteUpdateView.as_view(), name='expediente-update'),	
]