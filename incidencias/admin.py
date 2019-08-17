from django.contrib import admin
from .models import *

class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'fecha_solucion']
    search_fields = ['escuela',]
#    list_filter = ['region']
#    prepopulated_fields = {"slug": ("nombre",)}
admin.site.register(Incidencia, IncidenciaAdmin)