from django.shortcuts import render
from .models import Taller
from datetime import date

def inicio(request):
    talleres = Taller.objects.filter(estado='aceptado', fecha__gt=date.today())
    return render(request, 'talleres/inicio.html', {'talleres': talleres})
