from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import proveedorForm
from django.views.decorators import csrf
from rest_framework.serializers import Serializer
from .serializers import ProveedorSerializer
from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def form_proveedor(request):
   if request.method=='POST':
          proveedor_form = proveedorForm(request.POST,request.FILES)
          if proveedor_form.is_valid():
             proveedor_form.save()
             return redirect('home')
   else:
        proveedor_form=proveedorForm()    
   return render(request, 'core/Form_creaProveedor.html', {'proveedor_form':proveedor_form})


def Ver(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'core/Ver.html', context={'usuarios':proveedor})

def form_modificar(request,id):
    proveedor = Proveedor.objects.get(numIdentificacion=id)

    datos ={
        'form': proveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = proveedorForm(data=request.POST, instance = proveedor, files=request.FILES)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/Form_modProveedor.html', datos)

def form_eliminar(request,id):
    proveedor = Proveedor.objects.get(numIdentificacion=id)
    proveedor.delete()
    return redirect('ver')



'''Serializers '''


@csrf_exempt
@api_view(['GET', 'POST'])


def lista_proveedores(request):
    if request.method== 'GET':
        prove = Proveedor.objects.all()
        serializer = ProveedorSerializer(prove, many=True)
        return Response(serializer.data)

    elif request.method=='POST': 
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def lista_api(request):
    return render(request, 'ApiWeb.html')

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_proveedor(request,id): 
    try: 
        proveedor = Proveedor.objects.get(numIdentificacion=id) 
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET': 
        serializer = ProveedorSerializer(vehiculo)
        return Response(serializer.data)
    if request.method=='PUT': 
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(vehiculo, data = data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE': 
        proveedor.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)
