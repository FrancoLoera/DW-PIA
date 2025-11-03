from django.contrib import admin
from .models import TipoEvento, Reservacion, ReservacionShow

# Register your models here.
admin.site.register(TipoEvento)
admin.site.register(Reservacion)
admin.site.register(ReservacionShow)