from django.db import models

# Create your models here.
class biblioteca(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=120, verbose_name="titulo")
    img = models.ImageField(upload_to="imagenes/", null=True, verbose_name="imagenes")
    des = models.CharField(max_length=200, null=True, verbose_name="descripción")
    
    def __str__(self) -> str:
        fila = f"Nombre: {self.titulo} - Descripción: {self.des}"
        return fila