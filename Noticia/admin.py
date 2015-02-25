from django.contrib.admin import site
from Noticia.models import Noticia
from django.contrib import admin

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo","descripcion","estado")

site.register(Noticia,NoticiaAdmin)