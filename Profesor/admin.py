from django.contrib.admin import site
from Profesor.models import Profesor
from django.contrib import admin

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","cedula","direccion","telefono","correo","titulo")

site.register(Profesor,ProfesorAdmin)

