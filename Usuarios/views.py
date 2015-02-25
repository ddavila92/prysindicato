# -*- coding: utf-8 -*-
import random
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.core.mail.message import EmailMessage
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from Estudiantes.models import Estudiantes
from django.contrib import auth
import os
import time
from Noticia.models import Noticia
from Profesor.models import Profesor


def generar_captchat():
    cadena=""
    letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
    for i in range(0,6):
        aleatorio=random.randrange(0,35,3)
        print aleatorio
        cadena+=letras[aleatorio]
    print cadena
    return cadena

def lectura_host():
    archivo=open(os.path.dirname(__file__)+"/host.txt","r")
    linea=archivo.readline()
    print linea
    archivo.close()
    return linea

def registro_de_usuarios(request):
    captcha=generar_captchat()
    if request.POST:
        c=request.POST['captcha'].upper()
        c1=request.POST['captcha1']
        print c,captcha
        if c1==c and validar_cedula(request.POST['cedula']):
            try:
                user = User.objects.create_user(username=request.POST['email'],
                                                email=request.POST['email'],password=request.POST['password'],
                                                first_name=request.POST['nombres'], last_name=request.POST['apellidos'])

                user.is_staff=False
                user.is_active=False
                user.save()
                try:
                    print request.POST['fecha_nacimiento']
                    Estudiantes(usuario=user,cedula=request.POST['cedula'],fecha_nacimiento=request.POST['fecha_nacimiento'],
                                cert_votacion=request.POST['certificado_votacion'],nombre_colegio=request.POST['nombre_colegio'],
                                lugar_nacimiento=request.POST['lugar_nacimiento'],nacionalidad=request.POST['nacionalidad'],
                                telefono=request.POST['telefono'],tipo_sangre=request.POST['tipo_sangre'],anio_graduacion=request.POST['anio_graduacion'],
                                direccion=request.POST['direccion'],sexo=request.POST['sexo']).save()
                    host=str(lectura_host())
                    email = EmailMessage("- SINDICATO CANTONAL DE CHOFERES PROFESIONALES DE PASAJE -","\n\n\nTe damos la Bienvenida, y te agradecemos por registrarte en nuestro sistema, aqui tienes un enlace para activar tú cuenta: http://"+host+"/activar_usuario/"+str(user.id), to=[request.POST['email']])
                    email.send()
                except Exception as error:
                    print error
                    pass
                return render_to_response("public/Registro.html",{"mensaje":"Su cuenta fué creada exitosamente, LOS DATOS DE LA ACTIVACIÓN LLEGARÁN A SU CORREO ELECTRÓNICO..!!","captcha":captcha})
            except:
                return render_to_response("public/Registro.html",{"mensaje":"Se ha presentado un error desconocido, por favor intente más tarde..!!"})
        else:
            return render_to_response("public/Registro.html",{"mensaje":"No ha pasado la validación o su cédula no es correcta, Reintente..!!"})
    else:
        return render_to_response("public/Registro.html",{"captcha":captcha})

def activacion(request,n):
    try:
        user=User.objects.get(id=n)
        user.is_active=True
        user.is_staff=True
        user.save()
        return render_to_response("public/activacion.html",{"usuario": user,"mensaje":"Su cuenta fué activada, ya puedes iniciar sesión <a href='/'>Aquí</a>"})
    except:
        return render_to_response("public/activacion.html",{"mensaje":"El Usuario no existe..!!, Puedes registrarte si das clic <a href='/Usuarios/registro/'>aquí</a>"})


def index(request):
    if not request.user.is_authenticated():
        print "usuario no esta autenticado"
        if request.POST:
            try:
                user = auth.authenticate(username=request.POST['usuario'], password=request.POST['password'])
                if user is not None and user.is_active and not user.is_superuser:
                    try:
                        Profesor.objects.get(usuario=user)
                        auth.login(request, user)
                        print "Entro el Proffesor: ",user.username
                        return render_to_response("public/Profesores/datos_docente.html",{"usuario":request.user,"profesor":Profesor.objects.get(usuario=request.user)})
                    except:
                        auth.login(request, user)
                        print "entro un estudiante:",user.username
                        return render_to_response("freeme/index.html",{"usuario":request.user,"noticias":Noticia.objects.all()})
                elif user is not None and user.is_active and user.is_superuser:
                    auth.login(request, user)
                    print "Entro un admin:"
                    return render_to_response("freeme/index.html",{"usuario":request.user,"code":"1"})
                else:
                    return render_to_response("freeme/index.html",{"noticias":Noticia.objects.all()})
            except Exception as error1:
                print error1
                return render_to_response("freeme/index.html",{"mensaje": "Credenciales incorrectas o el usuario no existe..!!","noticias":Noticia.objects.all()})
        else:
            return render_to_response("freeme/index.html",{"noticias":Noticia.objects.all()})
    else:
        print "usuario esta autenticado", request.user
        return render_to_response("freeme/index.html",{"usuario":request.user,"noticias":Noticia.objects.all()})


def cerrar_sesion(request):
    auth.logout(request)
    print "cerro la sesion"
    return HttpResponseRedirect("/")

def micuenta(request):
    if request.user.is_authenticated() and not request.user.is_superuser:
        try:
            pro=Profesor.objects.get(usuario=request.user)
            print "es profesor"
            return render_to_response("public/Profesores/datos_docente.html",{"usuario":request.user,"profesor":pro})
        except:
            print "es un alumno"
            return render_to_response("private/micuentalogin.html",{"usuario": request.user})
    elif request.user.is_authenticated() and request.user.is_superuser:
        print "es un admin"
        return render_to_response("freeme/index.html",{"code":"1"})
    else:
        print "es visitante"
        return render_to_response("public/micuenta.html")
    

def informacion_usuario(request):
    est= Estudiantes.objects.get(usuario=request.user)
    user=User.objects.get(id=request.user.id)
    if request.POST:
        user.first_name=request.POST['nombres']
        user.last_name=request.POST['apellidos']
        user.save()
        est.anio_graduacion=request.POST['anio_graduacion']
        est.cert_votacion=request.POST['certificado_votacion']
        est.direccion=request.POST['direccion']
        est.lugar_nacimiento=request.POST['lugar_nacimiento']
        est.nacionalidad=request.POST['nacionalidad']
        est.nombre_colegio=request.POST['nombre_colegio']
        est.telefono=request.POST['telefono']
        est.tipo_sangre=request.POST['tipo_sangre']
        est.save()
        return render_to_response("private/misdatos.html",{"usuario":request.user,"estudiante":est,"msj":"Los datos han sido modificados...!!"})
    else:
        return render_to_response("private/misdatos.html",{"usuario":request.user,"estudiante":est})

def recod_policial(request):
    est= Estudiantes.objects.get(usuario=request.user)
    return render_to_response("public/recordpolicial.html",{"usuario":request.user,"estudiante":est})

def validar_cedula(ced):
    valores = [ int(ced[x]) * (2 - x % 2) for x in range(9) ]
    suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
    return int(ced[9]) == 10 - int(str(suma)[-1:])