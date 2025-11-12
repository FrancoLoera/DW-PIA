from django.shortcuts import render
from shows.models import OpcionDuracion

# Create your views here.
def index(request):
    opciones = OpcionDuracion.objects.select_related('show').all().order_by('show__nombre', 'duracion')
    return render(request, 'index.html', {'opciones': opciones})