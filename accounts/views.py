from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Direccionador(View):
	@method_decorator(login_required)
	def get(self, request):
		return redirect('escuelas:region-list',)