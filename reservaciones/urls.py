from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/gestion/', views.gestion_admin, name='gestion_admin'),
    path('admin/eliminar/<int:id>/', views.eliminar_reservacion, name='eliminar_reservacion'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/agregar/', views.agregar_reservacion, name='agregar_reservacion'),
    path('admin/actualizar/<int:id>/', views.actualizar_reservacion, name='actualizar_reservacion'),
    # AGREGA ESTA LÍNEA PARA TU VISTA DE EMPLEADO:
    path('empleado/gestion/', views.gestion_empleado, name='gestion_empleado'),

    # (la nueva URL para el formulario del empleado):
    path('empleado/actualizar/<int:id>/', views.actualizar_estatus_empleado, name='actualizar_estatus_empleado'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
