from django.urls import path
from Servicios.views import vistaEjemplo

#SERVICIOS - Aplicación
# Archivo opcional

urlpatterns = [
    path('ejemplo/', vistaEjemplo)
]