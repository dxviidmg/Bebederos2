from django.contrib import admin
from .models import *

class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ['escuela',]
    search_fields = ['escuela',]
admin.site.register(Expediente, ExpedienteAdmin)

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ['escuela',]
    search_fields = ['escuela',]
admin.site.register(Fotografia, FotografiaAdmin)