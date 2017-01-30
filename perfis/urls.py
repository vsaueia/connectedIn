from django.conf.urls import url
from perfis.views import index, exibir, convidar

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='perfil'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar, name='convite')
]