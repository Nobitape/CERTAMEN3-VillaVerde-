from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import Taller
from datetime import date

# Create your views here.

def main(request):
    return render(request, 'talleres/main.html')

def talleres(request):
    return render(request, 'talleres/talleres.html')



def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            tipo = request.POST.get('tipo_usuario')
            if tipo == 'funcionario':
                user.is_staff = True
            user.save()

            login(request, user)  # lo loguea automáticamente
            return redirect('main')  # o donde quieras redirigir

    return render(request, 'talleres/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'talleres/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')