from django.contrib.admin import site
from django.contrib import admin
from Materia.models import Materia, Profesor_Materia

class MateriaAdmin(admin.ModelAdmin):
    list_display = ("materia",)
    search_fields = ["materia"]
    list_filter = ["materia"]

class Profesor_MateriaAdmin(admin.ModelAdmin):
    list_display = ("materia","profesor")
    search_fields = ["materia"]
    list_filter = ["materia"]

site.register(Materia,MateriaAdmin)
site.register(Profesor_Materia,Profesor_MateriaAdmin)
