from django.urls import path
from .views import inicio  # Asegúrate de que esta vista existe

urlpatterns = [
    path('', inicio, name='inicio'),
]