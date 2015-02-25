# Create your views here.
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from Estudiantes.models import Estudiantes
from Materia.models import Materia, Profesor_Materia
from Matricula.models import Paralelo, Periodo, Seccion, Matricula
from Nota.models import Nota
from Profesor.models import Profesor


def publicacion_notas(request):
    try:
        usuario=User.objects.get(username=request.user)
        estudiante=Estudiantes.objects.get(usuario=usuario)
        notas=Nota.objects.filter(estudiante=estudiante)
        return render_to_response("private/misnotas.html",{"notas":notas,"usuario":request.user})
    except Exception as error:
        print error
        return render_to_response("private/misnotas.html",{"usuario":request.user})

def modificar_notas(request):
    usuario=User.objects.get(username=request.user)
    profesor=Profesor.objects.get(usuario=usuario)
    materia=Profesor_Materia.objects.filter(profesor=profesor)
    if request.POST:
        notas=Nota.objects.filter(materia=Materia.objects.get(id=request.POST['materia']))
        matriculas=Matricula.objects.filter(periodo=request.POST['periodo'],seccion=request.POST['seccion'],paralelo=request.POST['paralelo'])
        return render_to_response("public/Profesores/tabla_modificar_notas.html",{"notas": notas,"matriculas":matriculas})
    else:
        return render_to_response("public/Profesores/modificar_calificacione.html",{"notas":Nota.objects.all(),"paralelos":Paralelo.objects.all(),"periodos":Periodo.objects.all(),
                                                                                "secciones":Seccion.objects.all(),"materias":materia,"matriculas":Matricula.objects.all(),"usuario":request.user})

def modifica_notas_estudiantes(request):
    if request.POST:
        n=Nota.objects.get(id=request.POST['nota'])
        n.deber=request.POST['deber']
        n.actuacion=request.POST['actuacion']
        n.leccion=request.POST['leccion']
        n.examen=request.POST['examen']
        n.supletorio=request.POST['supletorio']
        n.save()
        usuario=User.objects.get(username=request.user)
        profesor=Profesor.objects.get(usuario=usuario)
        materias=Profesor_Materia.objects.filter(profesor=profesor)
        materia=Materia.objects.get(id=request.POST['materia'])
        notas=Nota.objects.filter(materia=materia)
        matriculas=Matricula.objects.filter(periodo=request.POST['periodo'],seccion=request.POST['seccion'],paralelo=request.POST['paralelo'])
        return render_to_response("public/Profesores/mod.html",{"notas":notas, "matriculas":matriculas,"materias":materias,"periodos":Periodo.objects.all(),"secciones":Seccion.objects.all(),
                                                                "paralelos":Paralelo.objects.all(),"usuario":request.user})
    else:
        HttpResponseRedirect("/Notas/modificar_notas/")
        

def actas_calificaciones(request):
    usuario=User.objects.get(username=request.user)
    profesor=Profesor.objects.get(usuario=usuario)
    materia=Profesor_Materia.objects.filter(profesor=profesor)
    if request.POST:
        materia=Materia.objects.get(id=request.POST['materia'])
        notas=Nota.objects.filter(materia=materia)
        matriculas=Matricula.objects.filter(periodo=request.POST['periodo'],seccion=request.POST['seccion'],paralelo=request.POST['paralelo'])
        return render_to_response("public/Profesores/tabla_modificar_notas.html",{"matriculas":matriculas,"notas": notas,"estado":"ok","usuario":request.user})
    else:
        return render_to_response("public/Profesores/actas.html",{"paralelos":Paralelo.objects.all(),"periodos":Periodo.objects.all(),
                                                                                "secciones":Seccion.objects.all(),"materias":materia,"usuario":request.user})

def imprimible(request, p,s,pa,m):
    materia=Materia.objects.get(id=m)
    notas=Nota.objects.filter(materia=materia)
    matriculas=Matricula.objects.filter(periodo=p,seccion=s,paralelo=pa)
    return render_to_response("public/Profesores/tabla_modificar_notas.html",{"matriculas":matriculas,"notas": notas,"estado":"ok","usuario":request.user})