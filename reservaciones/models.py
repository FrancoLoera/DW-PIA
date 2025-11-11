from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from shows.models import OpcionDuracion

# Modelo principal
class Reservacion(models.Model):
    
    ESTATUS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("realizada", "Realizada"),
    ]

    TIPOS_EVENTO = [
        ("cumpleaños", "Cumpleaños"),
        ("boda", "Boda"),
        ("xv", "XV Años"),
        ("infantil", "Evento Infantil"),
        ("corporativo", "Evento Corporativo"),
        ("otro", "Otro"),
    ]
    
    nombreCliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    fechaEvento = models.DateField(unique=True)
    numInvitados = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        help_text="1 a 50 invitados permitidos"
    )
    estatus = models.CharField(max_length=10, choices=ESTATUS, default="pendiente")
    tipoEvento = models.CharField(max_length=20, choices=TIPOS_EVENTO, default="cumpleaños")
    
    def __str__(self):
        return f"{self.nombreCliente} - {self.fechaEvento} ({self.get_estatus_display()})"

    def clean(self):
        super().clean()
        
        if self.pk:
            relaciones = self.reservacionshow_set.select_related('opcionDuracion__show')
            total_Minutos = 0
            tipos_Show = set()
            
            for r in relaciones:
                nombre_Show = r.opcionDuracion.show.nombre
                
                if nombre_Show in tipos_Show:
                    raise ValidationError("No se puede repetir el mismo tipo de show")
                tipos_Show.add(nombre_Show)
                
                duracion_str = r.opcionDuracion.duracion
                horas, minutos = map(int, duracion_str.split(":"))
                total_Minutos += (horas * 60) + minutos
                
            if total_Minutos > (8 * 60):
                raise ValidationError("La duración total de los shows no puede exceder 8 horas")


class ReservacionShow(models.Model):
    reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    opcionDuracion = models.ForeignKey(OpcionDuracion, on_delete=models.PROTECT)
    
    class Meta:
        unique_together = ("reservacion", "opcionDuracion")
        
    def __str__(self):
        return f"{self.reservacion.nombreCliente} - {self.opcionDuracion}"
