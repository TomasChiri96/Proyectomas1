from django.urls import path
from Barraps import views
from .views import inicio, vista_mozo, vista_mezas, vista_almacen


urlpatterns = [
    
    path('', inicio, name="Inicio"),
    path('vistamozos/', vista_mozo, name="Mozos"),
    path('vistamesas/', vista_mezas, name="Meza"),
    path('vistaalmacen/', vista_almacen)
]