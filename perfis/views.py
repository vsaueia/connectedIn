from django.shortcuts import render, redirect
from perfis.models import Perfil


def index(request):
    perfis = Perfil.objects.all()
    return render(request, 'index.html', {"perfis": perfis})


def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html', {"perfil": perfil})


def convidar(request, perfil_id):
    perfil_convidado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidado=perfil_convidado)
    return redirect('home')


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)
