from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Taller, Categoria
from datetime import date
from django.utils import timezone


def main(request):
    return render(request, 'talleres/main.html')

def listar_talleres(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria_id')

    talleres = Taller.objects.filter(
        estado='aceptado',
        fecha__gte=timezone.now().date()
    ).order_by('fecha')

    if categoria_id:
        talleres = talleres.filter(categoria_id=categoria_id)

    context = {
        'talleres': talleres,
        'categorias': categorias,
        'selected_categoria_id': int(categoria_id) if categoria_id else None
    }
    return render(request, 'talleres/talleres.html', context)

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return redirect('/') 

    else:
        form = UserCreationForm()
    return render(request, 'talleres/register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_superuser or user.is_staff:
                return redirect('/admin')

            elif user.groups.filter(name='Junta de Vecinos').exists():
                return redirect('/api/talleres')   

            else:
                return redirect('main')         
    else:
        form = AuthenticationForm()
    return render(request, 'talleres/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('main')