from django.conf.urls import url
from Enlaces.views import *

Enlace=[
    url(r'^prgacademico/$',prg_academico),
    url(r'^admision/$',admision),
    url(r'^servicios/$',servicios),
    url(r'^acerca_de/$',acerca_de),
    url(r'^docente/$',datos_docente),
]
