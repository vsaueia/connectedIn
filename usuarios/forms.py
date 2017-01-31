from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=False)
    nome_empresa = forms.CharField(required=False)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adicionar_erro('Por favor, verifique os dados informados')
            valid = False

        usuario_existente = User.objects.filter(username=self.data['nome']).exists()
        if usuario_existente:
            self.adicionar_erro('Usuario ja cadastrado')
            valid = False

        return valid

    def adicionar_erro(self, mensagem):
        erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(mensagem)
