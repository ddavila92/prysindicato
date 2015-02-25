from django.conf.urls import url
from Profesor.views import lista_alunos, cambiar_pass

Profesores=[
    url(r'^$',lista_alunos),
    url(r'^cambiar_pass/$',cambiar_pass),
]
