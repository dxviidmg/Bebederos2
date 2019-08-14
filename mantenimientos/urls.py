from django.urls import path
from .views import *

app_name = 'mantenimientos'

urlpatterns = [
	path('mantenimiento/update/<int:pk>/', MantenimientoUpdateView.as_view(), name='mantenimiento-update'),
	path('nuevo-mantenimiento/escuela/<slug:slug>/', MantenimientoCreateView.as_view(), name='mantenimiento-create'),
	path('escuela/<slug:slug>/mantenimientos/', MantenimientoListView.as_view(), name='mantenimiento-list'),
]