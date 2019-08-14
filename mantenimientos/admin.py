from django.contrib import admin
from .models import *

class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ['escuela',]
    search_fields = ['escuela',]
admin.site.register(Mantenimiento, MantenimientoAdmin)