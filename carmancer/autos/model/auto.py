from django.db import models

class Auto(models.Model):
    nombre = models.CharField(max_length=30)
    
    modelo = models.ForeignKey('autos.modelo',on_delete=models.CASCADE)

    