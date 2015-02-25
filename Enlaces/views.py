from django.shortcuts import render_to_response
from Profesor.models import Profesor


def prg_academico(request):
    if request.user.is_authenticated():
        return render_to_response("public/Programa_Academico.html",{"usuario":request.user})
    else:
        return render_to_response("public/Programa_Academico.html")
def admision(request):
    if request.user.is_authenticated():
        return render_to_response("public/Admision.html",{"usuario":request.user})
    else:
        return render_to_response("public/Admision.html")
def servicios(request):
    if request.user.is_authenticated():
        return render_to_response("public/servicios.html",{"usuario":request.user})
    else:
        return render_to_response("public/servicios.html")
def acerca_de(request):
    if request.user.is_authenticated():
        return render_to_response("public/acerca_de.html",{"usuario":request.user})
    else:
        return render_to_response("public/acerca_de.html")

def datos_docente(request):
    if request.user.is_authenticated():
        pro=Profesor.objects.get(usuario=request.user)
        return render_to_response("public/Profesores/datos_docente.html",{"usuario":request.user,"profesor":pro})