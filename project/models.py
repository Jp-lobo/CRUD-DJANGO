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

class users(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120, verbose_name="nombre")
    apellido = models.CharField(max_length=120, verbose_name="apellido")
    correo = models.EmailField(max_length=120, verbose_name="correo")
    telefono = models.CharField(max_length=120, verbose_name="telefono")
    
    def __str__(self) -> str:
        fila = f"{self.id} - {self.nombre} {self.apellido}"
        return fila

class prestamos(models.Model):
    id = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(biblioteca, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(users, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True, verbose_name="fecha_prestamo")
    fecha_devolucion = models.DateField(verbose_name="fecha_devolucion")
    estado = models.BooleanField(default=True, verbose_name="estado")
    
    def __str__(self) -> str:
        fila = f"Nombre: {self.id_libro} {self.id_usuario}"
        return fila