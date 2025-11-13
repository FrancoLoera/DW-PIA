from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservacion, TipoEvento
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import logout

# Página principal (dashboard admin)
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
@login_required
def agregar_reservacion(request):
    errores = []
    tipos_evento = TipoEvento.objects.all()

    if request.method == "POST":
        nombreCliente = request.POST["nombreCliente"].strip()
        telefono = request.POST["telefono"].strip()
        fechaEvento = request.POST["fechaEvento"].strip()
        numInvitados = request.POST["numInvitados"].strip()
        tipoEvento_id = request.POST["tipoEvento"]
        estatus = request.POST["estatus"]

        # Validaciones
        if not nombreCliente.replace(" ", "").isalpha():
            errores.append("El nombre solo puede contener letras y espacios.")

        if not (telefono.isdigit() and len(telefono) == 10):
            errores.append("El teléfono debe tener exactamente 10 dígitos y solo números.")

        try:
            fecha_evento_obj = datetime.strptime(fechaEvento, "%Y-%m-%d").date()
        except ValueError:
            errores.append("La fecha del evento no es válida.")

        # ✅ Convertir tipoEvento a objeto real
        try:
            tipoEvento = TipoEvento.objects.get(id=tipoEvento_id)
        except TipoEvento.DoesNotExist:
            errores.append("Selecciona un tipo de evento válido.")

        # Si no hay errores, crear la reservación
        if not errores:
            Reservacion.objects.create(
                nombreCliente=nombreCliente,
                telefono=telefono,
                fechaEvento=fecha_evento_obj,
                numInvitados=numInvitados,
                tipoEvento=tipoEvento,
                estatus=estatus,
            )
            messages.success(request, "Reservación agregada correctamente.")
            return redirect("gestion_admin")

    return render(request, "reservaciones/agregar.html", {
        "tipos_evento": tipos_evento,
        "errores": errores
    })


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
        reservacion.estatus = request.POST.get('estatus')

        # ✅ Obtener tipo de evento como objeto
        tipoEvento_id = request.POST.get('tipoEvento')
        if tipoEvento_id:
            reservacion.tipoEvento = get_object_or_404(TipoEvento, id=tipoEvento_id)

        reservacion.save()
        messages.success(request, "Reservación actualizada correctamente.")
        return redirect('gestion_admin')

    return render(request, 'reservaciones/actualizar.html', {
        'reservacion': reservacion,
        'tipos_evento': tipos_evento,
    })


@login_required
def eliminar_reservacion(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)
    reservacion.delete()
    messages.success(request, "Reservación eliminada correctamente.")
    return redirect('gestion_admin')


# VISTA PARA PÁGINA DE EMPLEADO
@login_required
def gestion_empleado(request):
    reservaciones = Reservacion.objects.all()
    return render(request, 'reservaciones/gestion_empleado.html', {'reservaciones': reservaciones})


# NUEVA VISTA: ACTUALIZAR ESTATUS (SOLO PARA EMPLEADO)
@login_required
def actualizar_estatus_empleado(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)

    if request.method == 'POST':
        reservacion.estatus = request.POST.get('estatus')
        reservacion.save()
        return redirect('gestion_empleado')

    return render(request, 'reservaciones/actualizar_empleado.html', {
        'reservacion': reservacion,
    })


def logout_view(request):
    logout(request)
    return redirect('index')
