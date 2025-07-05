from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'talleres/main.html')

def talleres(request):
    return render(request, 'talleres/talleres.html')