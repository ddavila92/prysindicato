from django.conf.urls import url
from Reportes.views import pdf_matricula, pdf_matricula1, reporte_promocion, promocion

Reporte=[
    url(r'^matricula/(\d+)/$',pdf_matricula),
    url(r'^matricula1/(\d+)/$',pdf_matricula1),
    url(r'^promocion/(\d+)/$',reporte_promocion),
    url(r'^promocion/$',promocion),
]