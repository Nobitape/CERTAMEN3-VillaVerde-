from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

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
            form.save()
            return redirect('register')

    contexto = {'form':form}
    return render(request, 'talleres/register.html', contexto)

def login(request):
    return render(request, 'talleres/login.html')
