from django.shortcuts import render, redirect, get_object_or_404

from .models import biblioteca, prestamos, users
from .form import formula

# Create your views here.
def nosotros(request):
    return render(request, "files/nosotros.html")

def editar(request, id):
    libro = biblioteca.objects.get(id=id)
    form = formula(request.POST or None, request.FILES or None, instance=libro)
    if form.is_valid() and request.POST:
        form.save()
        return redirect("libros")
    return render(request, "files/editar.html",{"formulario": form})

def estado(request, id):
    libro = biblioteca.objects.get(id=id)
    prestamo = prestamos.objects.filter(id_libro_id=id).order_by("-fecha_prestamo")
    estado = prestamos.objects.filter(id_libro_id=id,estado=True)
    if estado.exists():
        estado = " No Disponible"
    else:
        estado = " Disponible"
    return render(request, "files/estado.html",{"prestamos": prestamo,"libro":libro,"estado":estado})

def libros(request):
    biblio = biblioteca.objects.all()
    return render(request, "files/libros.html", {"libros":biblio})

def tabla(request): 
    form = formula(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("libros")
    return render(request, "files/tabla.html", {"formulario": form})

def eliminar(request, id):
    libro = biblioteca.objects.get(id=id)
    libro.delete()
    return redirect("libros")