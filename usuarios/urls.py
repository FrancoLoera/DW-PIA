
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Esta será tu URL personalizada para el login (ej: http://tusitio.com/entrar/)
    # Django buscará automáticamente un template en 'registration/login.html'
    path('entrar/', auth_views.LoginView.as_view(), name='login'),

    # Esta es la URL para 'Cerrar sesión' que usa tu header.html
    # (ej: http://tusitio.com/salir/)
    path('salir/', auth_views.LogoutView.as_view(), name='logout'),
]