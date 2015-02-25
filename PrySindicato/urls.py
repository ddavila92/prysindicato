from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Enlaces.url import Enlace
from Matricula.url import Matricula
from Nota.url import Notas
from Noticia.urls import Noticias
from Profesor.urls import Profesores
from Reportes.url import Reporte
from Turno.urls import Turnos
from Usuarios.url import Usuarios
from Usuarios.views import index, registro_de_usuarios, activacion

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^Usuarios/',include(Usuarios)),
    url(r'^Matricula/',include(Matricula)),
    url(r'^activar_usuario/(\d+)/$',activacion),
    url(r'^Reporte/',include(Reporte)),
    url(r'^Notas/',include(Notas)),
    url(r'^Enlace/',include(Enlace)),
    url(r'^Turnos/',include(Turnos)),
    url(r'^Noticias/',include(Noticias)),
    url(r'^Profesores/',include(Profesores)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
# esto es para que se puedan usar los archivos de media url
if settings.DEBUG:
    urlpatterns+=patterns('',url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}))

