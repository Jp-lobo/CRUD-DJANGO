from django.contrib import admin
from .models import biblioteca, users, prestamos
# Register your models here.
admin.site.register(biblioteca)
admin.site.register(users)
admin.site.register(prestamos)
