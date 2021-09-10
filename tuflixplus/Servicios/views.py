from django.shortcuts import render

# Para imprimir mensajes sencillos de respuesta:
from django.http import HttpResponse

# Create your views here.

def vistaEjemplo(request):
    '''
    request ->  contiene toda la info del user que hace la 
                peticion de acceso a la app a través de los 
                métodos GET y POST
    '''
    return HttpResponse('Hola, estás en la app Servicios')
