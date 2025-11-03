from django.db import models

class Show(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    descripcion = models.CharField(max_length = 100, null = False, blank = False)
    
    def __str__(self):
        return self.nombre
    
class OpcionDuracion(models.Model):
    DURACIONES = [
        ("00:30", "30 Minutos"),
        ("01:00", "1 Hora"),
        ("01:30", "1 Hora y 30 minutos"),
        ("02:00", "2 Horas"),
    ]
    
    show = models.ForeignKey(Show, on_delete =  models.CASCADE, related_name = "opciones")
    duracion = models.CharField(max_length = 5, choices = DURACIONES)
    precio = models.DecimalField(max_digits = 7, decimal_places = 2)
    
    def __str__(self):
        return f"{self.show.nombre} - {self.get_duracion_display()} (${self.precio})"