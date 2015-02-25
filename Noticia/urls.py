from django.conf.urls import url
from Noticia.views import noticias, detalle_noticia

Noticias=[
    url(r'^$',noticias),
    url(r'^(\d+)$',detalle_noticia),
]
