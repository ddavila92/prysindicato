from django.conf.urls import url
from Nota.views import publicacion_notas, modificar_notas, modifica_notas_estudiantes, actas_calificaciones, imprimible
from Profesor.views import registrar_nota

Notas=[
   url(r'^$',publicacion_notas),
   url(r'^registro/$',registrar_nota),
   url(r'^modificar_notas/$',modificar_notas),
   url(r'^modificar_notas_est/$',modifica_notas_estudiantes),
   url(r'^actas/$',actas_calificaciones),
   url(r'^imprimir/(\d+)/(\d+)/(\d+)/(\d+)/$',imprimible),
]
