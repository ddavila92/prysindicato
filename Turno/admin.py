from django.contrib.admin import site
from Turno.models import Turno, Tipo_Tramite
from django.contrib import admin

class TurnoAdmin(admin.ModelAdmin):
    list_display = ("estudiante","tipo_tramite","fecha",)


site.register(Turno,TurnoAdmin)
site.register(Tipo_Tramite)