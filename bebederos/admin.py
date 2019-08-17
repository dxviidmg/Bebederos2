from django.contrib import admin
from .models import *

#class ProveedorAdmin(admin.ModelAdmin):
#	list_display = ['nombre']
#	search_fields = ['escuela',]
#admin.site.register(Proveedor, ProveedorAdmin)

class SistemaPotabilizadorAdmin(admin.ModelAdmin):
	list_display = ['tipo']
#	search_fields = ['escuela',]
admin.site.register(SistemaPotabilizador, SistemaPotabilizadorAdmin)

class MuebleAdmin(admin.ModelAdmin):
	list_display = ['modelo']
#	search_fields = ['escuela',]
admin.site.register(Mueble, MuebleAdmin)

class SistemaBebederoAdmin(admin.ModelAdmin):
	list_display = ['escuela']
#	search_fields = ['escuela',]
admin.site.register(SistemaBebedero, SistemaBebederoAdmin)