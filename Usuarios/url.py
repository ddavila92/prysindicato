from django.conf.urls import url
from Usuarios.views import *

Usuarios=[
    url(r'^$',index),
    url(r'^registro/$',registro_de_usuarios),
    url(r'^cerrar/$',cerrar_sesion),
    url(r'^micuenta/$',micuenta),
    url(r'^micuenta/misdatos/$',informacion_usuario),
    url(r'^micuenta/record_policial/$',recod_policial),

]
