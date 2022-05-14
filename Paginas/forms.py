from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('nome', 'email', 'senha', 'data_criacao', 'descricao', 'mostrar', 'foto')
