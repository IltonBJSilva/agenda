from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
# Create your views here.
from core.models import Evento

def index(request):
    redirect('/agenda/')

def lista_eventos(request):
    #criar um request no banco para usuario
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #filtrar as informações para aparecer apenas a do usuario
    dados = {'eventos': evento}
    return render(request,'agenda.html', dados)


# def index(request):
#     return redirect('/agenda/') #redireciona a pagina principal ja na agenda