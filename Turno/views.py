# -*- coding: utf-8 -*-
from datetime import date, timedelta,datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.backends.postgresql_psycopg2.base import IntegrityError, DatabaseError
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from Estudiantes.models import Estudiantes
from Turno.models import Turno, Tipo_Tramite

import pytz

ecuador = pytz.timezone('America/Guayaquil')
dias = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"}


def turnos(request):
    d = date.today()
    estudiante = Estudiantes.objects.get(usuario=request.user)
    turno = Turno.objects.all()
    if request.POST:
        t_tramite = Tipo_Tramite.objects.get(id=request.POST['tipo_tramite'])
        try:
            tr=Turno.objects.get(estudiante=estudiante,tipo_tramite=t_tramite)
            return render_to_response("private/turnos.html", {"fecha": d, "dia": dias[d.weekday()],
                                                                  "tipo_tramite": Tipo_Tramite.objects.all(),
                                                                  "msj": "Usted ya tiene un turno pendiente para este trámite..!!",
                                                                  "usuario": request.user,"estudiante":estudiante,"turno":tr,"tipo":tr.tipo_tramite})
        except ObjectDoesNotExist:
            if len(turno)>0:
                fecha = turno_dia(turno[0].fecha.weekday())
                print "esta es la fecha: ",fecha
                tur=Turno(estudiante=estudiante, tipo_tramite=t_tramite,fecha=fecha).save()
                return render_to_response("private/turnos.html", {"fecha": d, "dia": dias[d.weekday()],
                                                                      "tipo_tramite": Tipo_Tramite.objects.all(),
                                                                      "msj": "El Turno se generó correctamente..!!",
                                                                      "usuario": request.user,"turno":turno[0],"estudiante":estudiante,"tipo":Tipo_Tramite.objects.get(id=1)})
            else:
                Turno(estudiante=Estudiantes.objects.get(id=1),tipo_tramite=t_tramite,fecha=datetime.now()).save()
                fecha = turno_dia(turno[0].fecha.weekday())
                print "esta es la fecha: ",fecha
                tur= Turno(estudiante=estudiante, tipo_tramite=t_tramite,fecha=fecha).save()
                return render_to_response("private/turnos.html", {"fecha": d, "dia": dias[d.weekday()],
                                                                      "tipo_tramite": Tipo_Tramite.objects.all(),
                                                                      "msj": "El Turno se generó correctamente..!!",
                                                                      "usuario": request.user,"turno":turno[0],"estudiante":estudiante,"tipo":Tipo_Tramite.objects.get(id=1)})
    else:
        return render_to_response("private/turnos.html",
                                  {"fecha": d, "dia": dias[d.weekday()], "tipo_tramite": Tipo_Tramite.objects.all(),
                                   "usuario": request.user,"estudiante":estudiante})


def turno_dia(dia):
    turno = Turno.objects.all().order_by("id").reverse()
    if dia == 5:
        print "último día: ", dias[dia]
        fecha_actual = ecuador.normalize(turno[0].fecha)
        if fecha_actual.time().hour > 16:
            fecha_actual = fecha_actual - timedelta(hours=8)
        fecha_nueva = fecha_actual + timedelta(hours=48)
        print "siguiente turno",fecha_nueva.strftime("%Y-%m-%d %H:%M:%S")
        return fecha_nueva

    elif dia == 6:
        print "último día: ", dias[dia]
        fecha_actual = ecuador.normalize(turno[0].fecha)
        if fecha_actual.time().hour > 16:
            fecha_actual = fecha_actual - timedelta(hours=8)
        fecha_nueva = fecha_actual + timedelta(hours=24)
        print "siguiente turno",fecha_nueva.strftime("%Y-%m-%d %H:%M:%S")
        return fecha_nueva
    else:
        try:
            print "último día: ", dias[dia], "es un dia laborable"
            fecha_actual = ecuador.normalize(turno[0].fecha)
            if fecha_actual.time().hour > 16:
                fecha_actual = fecha_actual - timedelta(hours=8)
                fecha_nueva = fecha_actual + timedelta(hours=72)
                print "siguiente turno",fecha_nueva.strftime("%Y-%m-%d %H:%M:%S")
                return fecha_nueva
            else:
                fecha_nueva = fecha_actual + timedelta(minutes=15)
                print "siguiente turno",fecha_nueva.strftime("%Y-%m-%d %H:%M:%S")
                return fecha_nueva
        except Exception as error:
            print error


def eliminar_turno(request,n):
    t= Turno.objects.get(id=n)
    t.delete()
    return  HttpResponseRedirect("/Turnos/")