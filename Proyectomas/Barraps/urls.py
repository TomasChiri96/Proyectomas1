from django.urls import path
from Barraps import views
from .views import BusquedaMozo, busqueda, formularioMozo, inicio, leerMozos, vista_mozo, vista_mezas, vista_almacen, mozo_nuevo


urlpatterns = [
    
    path('', inicio, name="Inicio"),
    path('vistamozos/', vista_mozo, name="Mozos"),
    path('vistamesas/', vista_mezas, name="Meza"),
    path('vistaalmacen/', vista_almacen),
    path('nuevo-mozo/<nombre>/<apellido>/<numero>', mozo_nuevo),
    path('formularioMozo/',formularioMozo,name="AgregarMozo"),
    path('busqueda-mozo/',BusquedaMozo),
    path('buscar/', busqueda),
    path('leerMozos/', leerMozos, name="leerMozos")
]