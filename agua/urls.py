from django.urls import path
from .views import *

app_name = 'agua'

urlpatterns = [
	path('nuevo-analisis/escuela/<slug:slug>/', AnalisisCreateView.as_view(), name='analisis-create'),
	path('update-analisis/<slug:slug>/', AnalisisUpdateView.as_view(), name='analisis-update'),	
]