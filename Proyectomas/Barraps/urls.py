from django.urls import path
from Barraps import views
from .views import inicio, mozo2, mozo, vista_mozo


urlpatterns = [
    path('mozo2/', mozo2),
    path('', views.inicio),
    path('vistamozos/', vista_mozo),
    path('vistamesas/', views.vista_mezas),
    path('vistaalmacen/', views.vista_almacen)
]