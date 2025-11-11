
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservacion, TipoEvento
from django.contrib.auth.decorators import login_required

# Página principal (tu dashboard)
@login_required
def gestion_admin(request):
    reservaciones = Reservacion.objects.all()
    return render(request, 'reservaciones/gestion_admin.html', {'reservaciones': reservaciones})


# CONSULTAR (lista todas las reservaciones)
@login_required
def consultar_reservaciones(request):
    reservaciones = Reservacion.objects.all()
    return render(request, 'reservaciones/consultar.html', {'reservaciones': reservaciones})


# AÑADIR (crear nueva reservación)
def agregar_reservacion(request):
    if request.method == "POST":
        nombreCliente = request.POST["nombreCliente"]
        telefono = request.POST["telefono"]
        fechaEvento = request.POST["fechaEvento"]
        numInvitados = request.POST["numInvitados"]
        tipoEvento_id = request.POST["tipoEvento"]
        estatus = request.POST["estatus"]

        tipo_evento = TipoEvento.objects.get(id=tipoEvento_id)

        Reservacion.objects.create(
            nombreCliente=nombreCliente,
            telefono=telefono,
            fechaEvento=fechaEvento,
            numInvitados=numInvitados,
            tipoEvento=tipo_evento,
            estatus=estatus,
        )

        return redirect("gestion_admin")

    tipos_evento = TipoEvento.objects.all()
    return render(request, "reservaciones/agregar.html", {"tipos_evento": tipos_evento})

# ACTUALIZAR (editar reservación existente)
@login_required
def actualizar_reservacion(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)
    tipos_evento = TipoEvento.objects.all()

    if request.method == 'POST':
        reservacion.nombreCliente = request.POST.get('nombreCliente')
        reservacion.telefono = request.POST.get('telefono')
        reservacion.fechaEvento = request.POST.get('fechaEvento')
        reservacion.numInvitados = request.POST.get('numInvitados')
        tipoEvento_id = request.POST.get('tipoEvento')
        reservacion.tipoEvento = TipoEvento.objects.get(id=tipoEvento_id)
        reservacion.estatus = request.POST.get('estatus')
        reservacion.save()
        return redirect('gestion_admin')

    for tipo in tipos_evento:
        tipo.es_seleccionado = (tipo.id == reservacion.tipoEvento.id)

    return render(request, 'reservaciones/actualizar.html', {
        'reservacion': reservacion,
        'tipos_evento': tipos_evento,
    })

@login_required
def eliminar_reservacion(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)
    reservacion.delete()

    return redirect('gestion_admin')



# VISTA PARA  PÁGINA DE EMPLEADO
@login_required
def gestion_empleado(request):
    reservaciones = Reservacion.objects.all()
    return render(request, 'reservaciones/gestion_empleado.html', {'reservaciones': reservaciones})

# NUEVA VISTA: ACTUALIZAR ESTATUS (SOLO PARA EMPLEADO)
@login_required
def actualizar_estatus_empleado(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)

    if request.method == 'POST':
        # El empleado SOLO puede cambiar el estatus
        reservacion.estatus = request.POST.get('estatus')
        reservacion.save()
        
        # Lo redirigimos de vuelta a SU página de gestión
        return redirect('gestion_empleado') 

    # Le pasamos solo la reservación, no necesitamos más
    return render(request, 'reservaciones/actualizar_empleado.html', {
        'reservacion': reservacion,
    })