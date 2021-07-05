from django.urls import path
from .views import home, form_proveedor

urlpatterns =[
    path('', home, name="home"),
    path('Form_creaproveedor', form_proveedor, name="crear")
]