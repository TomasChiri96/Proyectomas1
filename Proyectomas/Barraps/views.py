from django.http import HttpResponse
from django.shortcuts import render
from Barraps.models import mozo
from Barraps.forms import FormularioMozo



# Create your views here.
def mozo2(request):
    mozo2 = mozo(nombre = "Alfio", apellido = "Junior", numero = 2)
    mozo2.save()
    texto1 = f"Se agrego a {mozo2.nombre}, {mozo2.apellido} con el numero asignado: {mozo2.numero}"

    return HttpResponse(texto1)

def mozo_nuevo(request, nombre, apellido, numero):
    mozo_nuevo = mozo(nombre=nombre, apellido=apellido, numero=numero)
    mozo_nuevo.save()
       

    return render(request, 'AppBarraps/mozo_nuevo.html', {'nombre':nombre, "apellido":apellido, "numero":numero}) 


def inicio(request):
    
    return render(request, 'AppBarraps/inicio.html')

def vista_mozo(request):

    return render(request, 'AppBarraps/vistamozo.html')

def vista_mezas(request):

    return render(request, 'AppBarraps/vistameza.html')

def vista_almacen(request):

    return render(request, 'AppBarraps/vistaalmacen.html')

def formularioMozo(request):

    if request.method == 'POST':
        Miformulario = FormularioMozo(request.POST)

        if Miformulario.is_valid():

            informacion = Miformulario.cleaned_data
            
            guardarMozo = mozo(nombre=informacion['nombre'], apellido=informacion['apellido'], numero=informacion['numero'])
            
            guardarMozo.save()
            
            return render(request, "AppBarraps/mozo_nuevo.html")
    
    else:
        mi_formulario = FormularioMozo()
    return render(request, 'AppBarraps/formularioMozo.html', {"miFormulario":mi_formulario})

def BusquedaMozo(request):

    
    return render(request, 'AppBarraps/busquedaMozo.html')


def busqueda(request):

    if request.GET['apellido']:
        
        apellido = request.GET['apellido']
        
        nombre = mozo.objects.filter(apellido=apellido)

        return render (request, 'AppBarraps/busqueda.html', {"apellido":apellido, "nombre":nombre})

    else:
        respuesta = "No enviaste datos"
        

    
    return HttpResponse(respuesta)


def leerMozos(request):
    mozos = mozo.objects.all()
    contexto = {"Mozo":mozos}
    return render (request, 'AppBarraps/leerMozos.html', contexto)

    
    
