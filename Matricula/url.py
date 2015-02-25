from django.conf.urls import url
from Matricula.views import *

Matricula=[
    url(r'^estudiante/$',matricula),
    url(r'^id_paralelo/$',contador),
]
