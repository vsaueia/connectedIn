from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite


def index(request):
    perfis = Perfil.objects.all()
    perfil_logado = get_perfil_logado(request)
    return render(request, 'index.html', {"perfis": perfis, "perfil_logado": perfil_logado})


def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()

    return render(request, 'perfil.html', {"perfil": perfil, "ja_eh_contato": ja_eh_contato})


def convidar(request, perfil_id):
    perfil_convidado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidado=perfil_convidado)
    return redirect('home')


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)


def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('home')
