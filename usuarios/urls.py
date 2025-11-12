from django.urls import path
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import views

def cerrar_sesion(request):
    logout(request)
    return redirect('index')  

urlpatterns = [
    path('login/', views.login_personalizado, name='login_personalizado'),
    path('logout/', cerrar_sesion, name='cerrar_sesion'),  
]
