from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("", views.nosotros, name="nosotros"),
    path("libros/", views.libros, name="libros"),
    path("tabla/", views.tabla, name="tabla"),
    path("editar/", views.editar, name="editar"),
    path("libros/editar/<int:id>", views.editar, name="editar"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
