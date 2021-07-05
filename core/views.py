from django.shortcuts import render
from .models import Proveedor
from .forms import proveedorForm

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def form_proveedor(request):
   if request.method=='POST':
          proveedor_form = proveedorForm(request.POST)
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
    proveedor = Proveedor.objects.get(nroChip=id)

    datos ={
        'form': proveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = proveedorForm(data=request.POST, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/Form_ModProveedor.html', datos)

def form_eliminar(request,id):
    proveedor = Proveedor.objects.get(nroChip=id)
    proveedor.delete()
    return redirect('ver')