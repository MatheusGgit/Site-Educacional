from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('login/', views.index, name='index'),
    path('Site_Educacional/', views.Site_Educacional, name='Site_Educacional'),
    path('Perfil/', views.Perfil, name='Perfil'),
    path('MeuAprendizado/', views.MeuAprendizado, name='MeuAprendizado'),
    path('Catalogo/', views.Catalogo, name='Catalogo'),
    path('Cadastro/', views.Cadastro, name='Cadastro'),
    path('Redefinicao/', views.Redefinicao, name='RedefinicaoSenha'),
    path('Recuperacao/', views.Recuperacao, name='RecuperacaoSenha'),
    path('ComprarCursos/<int:curso_id>', views.ComprarCurso, name='ComprarCurso'),
    path('PlayerVideo/<int:curso_id>', views.PlayerVideo, name='PlayerVideo'),
    path('logout/', views.Logout, name='Logout'),
    path('busca/>', views.busca, name='busca'),
    path('RedefiniçãoNome', views.redefNome, name='redefNome'),
    path('RedefiniçãoDescrição', views.redefDesc, name='redefDesc'),
    path('RedefiniçãoFoto', views.redefPhoto, name='redefPhoto'),
]
