from django.contrib import admin
from .models import *

class AnalisisAdmin(admin.ModelAdmin):
	list_display = ['escuela', 'numero']
	search_fields = ['escuela',]
admin.site.register(Analisis, AnalisisAdmin)

class DictamenAdmin(admin.ModelAdmin):
	list_display = ['nombre']
	search_fields = ['nombre',]
admin.site.register(Dictamen, DictamenAdmin)