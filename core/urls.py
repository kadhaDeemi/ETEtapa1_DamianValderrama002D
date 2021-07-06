from django.urls import path
from .views import home, form_proveedor, Ver, form_modificar,form_eliminar

urlpatterns =[
    path('', home, name="home"),
    path('Form_creaproveedor', form_proveedor, name="crear"),
    path('Ver', Ver, name="ver"),
    path('Form_modProveedor/<id>/', form_modificar, name="Modificar"),
    path('form_eliminar/<id>/', form_eliminar, name="Eliminar")
]