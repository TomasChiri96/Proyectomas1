from django import forms


class FormularioMozo(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    numero = forms.IntegerField()

    