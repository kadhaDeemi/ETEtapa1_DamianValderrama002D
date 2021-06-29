from django.db import models

# Create your models here.

class Moneda(models.Model):
    idMoneda=models.IntegerField(primary_key=True, verbose_name='Id de Moneda')
    nomMoneda=models.CharField(max_length=50, verbose_name='Nombre de la moneda')

    def __str__(self):
        return(self.nomMoneda)

class Proveedor(models.Model):
    numIdentificacion=models.IntegerField(primary_key=True, max_length=20, verbose_name='Numero de identificacion')
    foto=models.FileField(null=True, blank=True)
    nomCompleto=models.CharField(max_length=100, verbose_name='Nombre proveedor')
    telefono=models.IntegerField(verbose_name='Numero de telefono')
    direccion=models.CharField(max_length=100, verbose_name='Direccion proveedor')
    email=models.CharField(max_length=100, verbose_name='Email')
    pais=models.CharField(max_length=100, verbose_name='Pais')
    contraseña=models.CharField(max_length=100, verbose_name='Contraseña')
    moneda=models.ForeignKey(Moneda, on_delete=models.CASCADE)


    def __int__(self):
        return(self.numIdentificacion)




