from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class marcas(models.Model):
    tiposmarcas = {
        'C':'COMBINACION DE COLORES',
        'D':'DENOMINATIVA',
        'E':'SECUENCIAL',
        'F':'FIGURATIVA',
        'G':'GUSTATIVA',
        'L':'TACTIL',
        'M':'MIXTA',
        'O':'OLFATIVA',
        'P':'POSICION',
        'R':'TRIDIMENSIONAL MIXTA',
        'S':'SONORA',
        'T':'TRIDIMENSIONAL'
        }
    tipo = models.CharField(max_length=1, choices=tiposmarcas.items())
    denominacion = models.CharField(max_length=100)
    fechapresentacion = models.DateField()
    fechaotorgamiento = models.DateField()
    
        
class mdindustriales(models.Model):
    tipomd = {
        'M':'MODELO INDUSTRIAL',
        'D':'DISEÑO INDUSTRIAL'
    }
    
    tipo = models.CharField(max_length=1, choices=tipomd.items())
    denominacion = models.CharField(max_length=100)
    fechapresentacion = models.DateField()
    fechaotorgamiento = models.DateField()

class pmu(models.Model):
    pmu = {
        'M':'MODELO DE UTILIDAD',
        'P':'PATENTE DE INVENCION'
    }
    
    tipo = models.CharField(max_length=1, choices=pmu.items())
    denominacion = models.CharField(max_length=100)
    fechapresentacion = models.DateField()
    fechaotorgamiento = models.DateField()

class obrasysoftware(models.Model):
    oys = {
        'O':'OBRAS LITERARIAS',
        's':'SOFTWARE'
    }
    
    tipo = models.CharField(max_length=1, choices=oys.items())
    denominacion = models.CharField(max_length=100)
    fechadeposito = models.DateField()
    fechaconstancia = models.DateField()

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"