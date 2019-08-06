from django.contrib import admin
from .models import *
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User
#from bebederos.models import *

#Regiones
class RegionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero']
    search_fields = ['nombre',]
admin.site.register(Region, RegionAdmin)

#Convocatorias
class ConvocatoriaAdmin(admin.ModelAdmin):
    list_display = ['año',]
#    search_fields = ['nombre',]
admin.site.register(Convocatoria, ConvocatoriaAdmin)

#Entidades
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'partida',]
    search_fields = ['nombre',]
    list_filter = ['region']
#    prepopulated_fields = {"slug": ("nombre",)}
admin.site.register(Entidad, EntidadAdmin)

class EntidadConvocatoriaAdmin(admin.ModelAdmin):
    list_display = ['entidad', 'convocatoria']
#    search_fields = ['nombre',]
#    list_filter = ['region']
#    prepopulated_fields = {"slug": ("nombre",)}
admin.site.register(EntidadConvocatoria, EntidadConvocatoriaAdmin)

class EscuelaAdmin(admin.ModelAdmin):
    list_display = ['cct', 'nombre']
#    search_fields = ['nombre',]
#    list_filter = ['region']
#    prepopulated_fields = {"slug": ("nombre",)}
admin.site.register(Escuela, EscuelaAdmin)