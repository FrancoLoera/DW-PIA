from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from reservaciones.models import Reservacion

@receiver(post_migrate)
def crear_grupos_roles(sender, **kwargs):
    # Crear grupos
    admin_group, _ = Group.objects.get_or_create(name='Administrativo')
    empleado_group, _ = Group.objects.get_or_create(name='Empleado')

    # Obtener tipo de contenido del modelo Reservacion
    content_type = ContentType.objects.get_for_model(Reservacion)

    # Permisos disponibles: add, change, delete, view
    permisos_admin = Permission.objects.filter(content_type=content_type)
    permisos_empleado = Permission.objects.filter(
        content_type=content_type,
        codename__in=['view_reservacion', 'change_reservacion']
    )

    # Asignar permisos
    admin_group.permissions.set(permisos_admin)
    empleado_group.permissions.set(permisos_empleado)
