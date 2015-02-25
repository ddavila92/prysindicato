# -*- coding: utf-8 -*-
from datetime import date
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi,os
from Matricula.models import *
import logging
from Nota.models import Nota

logging.basicConfig()
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def fetch_resources(uri, rel):
    path = ''
    return path

def write_to_pdf(template_src, context_dict, filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
    if not pdf.err:
        response = http.HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
        response.write(result.getvalue())
        return response
    return http.HttpResponse('Problema al Generar el Reporte: %s' % cgi.escape(html))

def pdf_matricula(request,n):
    mat=Matricula.objects.get(id=n)
    cadena=str(os.path.join("static","imgs/logo.png"))
    #return write_to_pdf('objetos/Matriculas/Matricula.html', {'matricula': mat,"fecha":date.today()}, 'Matricula')
    return render_to_response("objetos/Matriculas/Matricula.html",{'matricula': mat,"fecha":date.today()})

def pdf_matricula1(request,n):
    mat=Matricula.objects.get(id=n)
    return write_to_pdf('objetos/Matriculas/Matricula.html', {'matricula': mat,"fecha":date.today()}, 'Matricula')

def reporte_promocion(request,periodo):
    promosion=Matricula.objects.filter(periodo=periodo)
    return render_to_response("Reportes/promocion.html",{"promocion": promosion})

def promocion(request):

    if request.POST:
        promosion=Matricula.objects.filter(periodo=request.POST['periodo'],paralelo=request.POST['paralelo'])
        print promosion
        lista_notas=[]
        for alumno in promosion:
            promedio=0
            observacion=""
            for n in Nota.objects.all():
                nota=Nota.objects.get(estudiante=alumno.estudiante)
                promedio+=(nota.actuacion+nota.deber+nota.examen+nota.leccion)/4
                print promedio
            if promedio>=14:
                observacion="Aprobado"
            else:
                observacion="Reprobado"
            lista_notas.append({"alumno":alumno.estudiante.usuario.last_name +" " + alumno.estudiante.usuario.first_name,"cedula":alumno.estudiante.cedula ,"observacion":observacion})
        return render_to_response("Reportes/promocion.html",{"observacion":lista_notas})
    else:
        paralelos=Paralelo.objects.all()
        periodos=Periodo.objects.all()
        return render_to_response("Reportes/prametros_promocion.html",{"periodos":periodos,"paralelos":paralelos})