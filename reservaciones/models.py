from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.
class TipoEvento(models.Model):
    nombre = models.CharField(max_length = 50, unique = True)
    
    def __str__(self):
        return self.nombre

class Reservacion(models.Model):
    
    ESTATUS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("realizada", "Realizada"),
    ]
    
    nombreCliente = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 10, validators = [MinLengthValidator(10)])
    fechaEvento = models.DateField(unique = True)
    numInvitados = models.PositiveSmallIntegerField(validators = [MinValueValidator(1), MaxValueValidator(50)], help_text = "1 a 50 invitados permitidos")
    estatus = models.CharField(max_length = 10, choices = ESTATUS, default = "pendiente")
    tipoEvento = models.ForeignKey(TipoEvento, on_delete = models.PROTECT)
    
    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha_evento} ({self.get_estatus_display()})"
    
    # def clean(self):
    #     super().clean()
        
    #     if self.pk:
    #         relaciones = self.reservacionshow_set.select_related('opcionDuracion__show')
    #         total_Minutos = 0
    #         tipos_Show = set()
            
    #         for r in relaciones:
    #             # Validar que no se repita el mismo tipo de show. Tampoco se puede repetir el mismo tipo de show con distinta duración
    #             nombre_Show = r.opcionDuracion.duracion.show.nombre
                
    #             if nombre_Show in tipos_Show:
    #                 raise ValidationError("No se puede repetir el mismo tipo de show")
    #             tipos_Show.add(nombre_Show)
                
    #             duracion_str = r.opcionDuracion.duracion
    
class ReservacionShow(models.Model):
    reservacion = models.ForeignKey(Reservacion, on_delete = models.CASCADE)
    