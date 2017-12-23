from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def exibir(request, perfil):

    perfilCreated = Perfil.objects.get(id=perfil)


    return render(request, 'perfil.html', {"perfil": perfilCreated})


def convidar(request, perfil):
    pass
