from django.urls import path
from .views import *

app_name = 'bebederos'

urlpatterns = [
#	path('nuevo-expediente/escuela/<slug:slug>/', ExpedienteCreateView.as_view(), name='expediente-create'),
	path('update-sistemabebedero/<slug:slug>/', SistemaBebederoUpdateView.as_view(), name='sistemabebedero-update'),	
]