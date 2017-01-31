from django.conf.urls import url
from perfis import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='perfil'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convite'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar_convite')
]