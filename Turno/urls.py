from django.conf.urls import url
from Turno.views import turnos, eliminar_turno

Turnos=[
    url(r'^$',turnos),
    url(r'^eliminar/(\d+)$',eliminar_turno),
]
