from django.contrib.admin import site
from Matricula.models import *
from django.contrib import admin

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("estudiante","periodo","seccion","paralelo")

class ParaleloAdmin(admin.ModelAdmin):
    list_display = ("paralelo","cupo",)


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ("fecha_inicio","fecha_fin")

site.register(Matricula,MatriculaAdmin)
site.register(Periodo,PeriodoAdmin)
site.register(Seccion)
site.register(Paralelo,ParaleloAdmin)
