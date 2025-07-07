from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('register', views.registerView, name='register'),
    path('listar_talleres', views.listar_talleres, name='listar_talleres'), 
    path('logout', views.logoutView, name='logout'),    
]