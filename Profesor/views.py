# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from Estudiantes.models import Estudiantes
from Materia.models import Materia, Profesor_Materia
from Matricula.models import Periodo, Seccion, Paralelo, Matricula
from Nota.models import Nota
from Profesor.models import Profesor
def lista_alunos(request):
    usuario=User.objects.get(username=request.user)
    profesor=Profesor.objects.get(usuario=usuario)
    materia=Profesor_Materia.objects.filter(profesor=profesor)
    periodo=Periodo.objects.all()
    seccion=Seccion.objects.all()
    paralelo=Paralelo.objects.all()
    if request.POST:
        p=Periodo.objects.get(id=request.POST['periodo'])
        s=Seccion.objects.get(id=request.POST['seccion'])
        pa=Paralelo.objects.get(id=request.POST['paralelo'])
        matricula=Matricula.objects.filter(periodo=p,seccion=s,paralelo=pa)
        notas=Nota.objects.filter(materia=Materia.objects.get(id=request.POST['materia']))
        nota=[nota.estudiante.id for nota in notas]
        print nota
        iguales=[]
        if len(nota)>0:
            for m in matricula:
                if not m.estudiante.id in nota:
                    iguales.append(m)
                    print "no esta"
                else:
                    print "si esta"
            return render_to_response("public/Profesores/tabla_estudiantes.html",{"matriculas":iguales,"notas":notas})
        else:
            return render_to_response("public/Profesores/tabla_estudiantes.html",{"matriculas":matricula,"notas":notas})
    else:
        return render_to_response("public/Profesores/Profesores.html",{"usuario":usuario,"profesor":profesor,"materias":materia,"periodos":periodo,"secciones":seccion,"paralelos":paralelo})

def registrar_nota(request):
    materia=Materia.objects.get(id=request.POST['materia'])
    estudiante=Estudiantes.objects.get(id=request.POST['estudiante'])
    deber=request.POST['deber']
    leccion=request.POST['leccion']
    actuacion=request.POST['actuacion']
    examen=request.POST['examen']
    supletorio=request.POST['supletorio']
    Nota(materia=materia,estudiante=estudiante,deber=deber,leccion=leccion,actuacion=actuacion,examen=examen,supletorio=supletorio).save()
    p=Periodo.objects.get(id=request.POST['periodo'])
    s=Seccion.objects.get(id=request.POST['seccion'])
    pa=Paralelo.objects.get(id=request.POST['paralelo'])
    matricula=Matricula.objects.filter(periodo=p,seccion=s,paralelo=pa)
    notas=Nota.objects.filter(materia=Materia.objects.get(id=request.POST['materia']))
    nota=[nota.estudiante.id for nota in notas]
    print nota
    iguales=[]
    if len(nota)>0:
        for m in matricula:
            if not m.estudiante.id in nota:
                iguales.append(m)
                print "no esta"
            else:
                print "si esta"
        return render_to_response("public/Profesores/tabla_estudiantes.html",{"matriculas":iguales,"notas":notas})
    else:
        render_to_response("public/Profesores/tabla_estudiantes.html",{"matriculas":matricula,"notas":notas})

def cambiar_pass(request):
    print "usuario: ",request.user
    if request.POST:
        print "usuario: ",request.user
        print "contraseñas nuevas: ",request.POST['password1'],request.POST['password2']
        usuario=User.objects.get(username=request.user)
        if request.POST['password1']==request.POST['password2'] and usuario.check_password(request.POST['password']):
            usuario.set_password(request.POST['password1'])
            usuario.save()
            return render_to_response("public/cambiar_clave.html",{"msj":"Su clave fué cambiada con éxito","usuario":request.user})
        else:
            return render_to_response("public/cambiar_clave.html",{"msj":"Las contraseñas no coinciden o su clave anterior no es correcta..!!","usuario": request.user})
    else:
        return render_to_response("public/cambiar_clave.html",{"usuario": request.user})
