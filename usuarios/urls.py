from django.urls import path
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import views

def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # 👈 redirige a tu página principal

urlpatterns = [
    path('login/', views.login_personalizado, name='login'),
    path('logout/', cerrar_sesion, name='cerrar_sesion'),  # 👈 aquí está el cambio
]
