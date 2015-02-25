# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from Estudiantes.models import Estudiantes
from Matricula.models import Paralelo, Seccion, Periodo, Matricula


def matricula(request):
    if request.POST:
        if int(request.POST['contador1'])>0:
            usuario=User.objects.get(id=request.user.id)
            print usuario
            estudiante=Estudiantes.objects.get(usuario=usuario)
            try:
                Matricula.objects.get(estudiante=estudiante)
                return render_to_response("private/matriculas.html",{"usuario":request.user,"paralelos":Paralelo.objects.all(),"secciones":Seccion.objects.all(),"periodos":Periodo.objects.all(),"msj":"Usted ya esta matriculado en uno de los paralelos"})
            except:
                mat=Matricula(estudiante=estudiante,periodo=Periodo.objects.get(id=request.POST['periodo']),
                            seccion=Seccion.objects.get(id=request.POST['seccion']),
                            paralelo=Paralelo.objects.get(id=request.POST['paralelo']),estado=False)
                mat.save()
                return render_to_response("private/matriculas.html",{"usuario":request.user,"paralelos":Paralelo.objects.all(),"secciones":Seccion.objects.all(),"periodos":Periodo.objects.all(),"msj":"La Matricula en este curso se genero exitosamente..!!","matricula":mat})
        else:
            return render_to_response("private/matriculas.html",{"usuario":request.user,"paralelos":Paralelo.objects.all(),"secciones":Seccion.objects.all(),"periodos":Periodo.objects.all(),"msj":"Este curso ya esta lleno, intente con otro"})
    else:
        try:
            estudiante=Estudiantes.objects.get(usuario=request.user)
            mat=Matricula.objects.get(estudiante=estudiante)
            return render_to_response("private/matriculas.html",{"usuario":request.user,"paralelos":Paralelo.objects.all(),"secciones":Seccion.objects.all(),"periodos":Periodo.objects.all(),"matricula":mat})
        except:
            return render_to_response("private/matriculas.html",{"usuario":request.user,"paralelos":Paralelo.objects.all(),"secciones":Seccion.objects.all(),"periodos":Periodo.objects.all()})
def contador(request):
    n=request.POST['id_paralelo']
    paralelo=Paralelo.objects.get(id=n)
    mat=Matricula.objects.filter(paralelo=paralelo)
    print len(mat)
    cupo=paralelo.cupo-len(mat)
    return render_to_response("objetos/id_paralelo.html",{"contador":cupo})