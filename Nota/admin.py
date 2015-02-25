from django.contrib.admin.sites import site
from Nota.models import Nota
from django.contrib import admin
class NotaAdmin(admin.ModelAdmin):
    list_display = ("materia","estudiante","deber","actuacion","leccion","examen","supletorio")
site.register(Nota,NotaAdmin)

