from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Taller
from datetime import date


def main(request):
    return render(request, 'talleres/main.html')

def talleres(request):
    return render(request, 'talleres/talleres.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return redirect('/login') 

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

def logout(request):
    logout(request)
    return redirect('login')