from django.contrib import admin
from .models import Reservacion, ReservacionShow, TipoEvento

# Register your models here.
admin.site.register(Reservacion)
admin.site.register(ReservacionShow)
admin.site.register(TipoEvento)