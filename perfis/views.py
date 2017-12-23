from django.shortcuts import render, redirect
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def exibir(request, perfil):

    perfilCreated = Perfil.objects.get(id=perfil)


    return render(request, 'perfil.html', {"perfil": perfilCreated})


def convidar(request, perfil):
    perfil_convidado = Perfil.objects.get(id=perfil)
    perfil_logado = get_perfilLogado(request)
    perfil_logado.convidar(perfil_convidado)
    return redirect('index')

def get_perfilLogado(request):
    return Perfil.objects.get(id=1)
