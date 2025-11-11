from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/gestion/', views.gestion_admin, name='gestion_admin'),
    path('admin/eliminar/<int:id>/', views.eliminar_reservacion, name='eliminar_reservacion'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/consultar/', views.consultar_reservaciones, name='consultar_reservaciones'),
    path('admin/agregar/', views.agregar_reservacion, name='agregar_reservacion'),
    path('admin/actualizar/<int:id>/', views.actualizar_reservacion, name='actualizar_reservacion'),
]

