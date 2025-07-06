from django.contrib import admin
from .models import Categoria, Lugar, Profesor, Taller

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

class LugarAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'direccion']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_completo']

class TallerAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'estado', 'profesor', 'lugar', 'categoria']
    list_filter = ['estado', 'fecha', 'categoria']
    search_fields = ['titulo', 'observacion']