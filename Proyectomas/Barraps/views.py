from django.http import HttpResponse
from django.shortcuts import render
from Barraps.models import mozo


# Create your views here.
def mozo2(request):
    mozo2 = mozo(nombre = "Alfio", apellido = "Junior", numero = 2)
    mozo2.save()
    texto1 = f"Se agrego a {mozo2.nombre}, {mozo2.apellido} con el numero asignado: {mozo2.numero}"

    return HttpResponse(texto1)

def inicio(request):

    return render(request, 'AppBarraps/inicio.html')

def vista_mozo(request):

    return render(request, 'AppBarraps/vistamozo.html')

def vista_mezas(request):

    return render(request, 'AppBarraps/vistameza.html')

def vista_almacen(request):

    return render(request, 'AppBarraps/vistaalmacen.html')
