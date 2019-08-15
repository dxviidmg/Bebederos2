from django.urls import path
#from django.contrib.auth import login, logout
#from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
	path('login', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
#	path('login', login.as_view(), name='login'),
#	path('logout', login, name='logout'),	

	path('accounts/direccionador', views.Direccionador.as_view(), name="direccionador"),
    ]