# Create your views here.
from django.shortcuts import render_to_response
from Noticia.models import Noticia


def noticias(request):
    noticia=Noticia.objects.all()
    if request.user.is_authenticated():
        return render_to_response("public/Noticias/Noticias.html",{"noticias":noticia,"usuario":request.user})
    else:
        return render_to_response("public/Noticias/Noticias.html",{"noticias":noticia})

def detalle_noticia(request,n):
    noticia=Noticia.objects.get(id=n)
    if request.user.is_authenticated():
        return render_to_response("public/Noticias/detalle_noticia.html",{"noticia":noticia,"usuario":request.user})
    else:
        return render_to_response("public/Noticias/detalle_noticia.html",{"noticia":noticia})