from django.urls import path
from .views import home, form_proveedor, Ver, form_modificar,form_eliminar,lista_proveedores, lista_api, detalle_proveedor


urlpatterns =[
    path('', home, name="home"),
    path('Form_creaproveedor', form_proveedor, name="crear"),
    path('Ver', Ver, name="ver"),
    path('Form_modProveedor/<id>/', form_modificar, name="Modificar"),
    path('form_eliminar/<id>/', form_eliminar, name="Eliminar"),
    path('lista_proveedores', lista_proveedores, name="lista_proveedores"),
    path('lista_api', lista_api, name="lista_api"),
    path('detalle_proveedor/<id>', detalle_proveedor, name="detalle_proveedor")
]