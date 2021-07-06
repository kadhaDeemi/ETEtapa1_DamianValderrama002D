from django import forms 
from django.forms import ModelForm, widgets
from .models import Proveedor

class proveedorForm(ModelForm):
     class Meta:
        model= Proveedor
        fields = ['numIdentificacion', 'foto', 'nomCompleto', 'telefono', 'direccion', 'email','pais','contraseña','moneda']
        labels ={
            'numIdentificacion':'Ingrese numero de identificación',
            'foto': ' Ingrese foto de logo empresa',
            'nomCompleto': '  Ingrese nombre de completo',
            'telefono': '   Indique numero telefono/celular',
            'direccion': '   Indique dirección ',
            'email': '   Ingrese su email',
            'pais': '   Ingrese su nacionalidad',
            'contraseña': '   Ingrese contraseña',
            'moneda': '   Ingrese el tipo moneda'            
        }
        widgets={
            'numIdentificacion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Numero identificación',
                    'id': 'numIdentificacion'
                }
            ),
            'foto': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'foto',
                    'id': 'foto'
                }
            ),
            'nomCompleto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Nombre completo',
                    'id': 'nomCompleto'
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Numero de telefono',
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese direccion',
                    'id': 'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese email',
                    'id': 'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el pais',
                    'id': 'pais'
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la contraseña',
                    'id': 'contraseña'
                }
            ),
            'moneda': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Seleccione el tipo moneda',
                    'id': 'moneda'
                }
            )
        }