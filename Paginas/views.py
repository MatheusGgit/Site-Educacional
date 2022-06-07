from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.validators import validate_email
from django.contrib import messages
from hashlib import *
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Usuarios, Cursos, Video, CursosFavorito, AulaAssistida
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse
import random
import os
import json

# Páginas - não é possível acessar sem estar logado
def Site_Educacional(request):
    if not request.session['login']:
        return redirect('landingPage')
    email = request.session['email']
    user = get_object_or_404(Usuarios, email=email)
    max_Cursos = Cursos.objects.all().count()

    ids = []
    for x in range(3):
        ids.append(random.randint(1, max_Cursos))
    curso = Cursos.objects.filter(id__in = ids)
    return render(request, 'Paginas/Site_Educacional.html', {'Usuarios': user, 'Cursos': curso})

def Perfil(request):
    if not request.session['login']:
        return redirect('landingPage')

    email = request.session['email']
    user = get_object_or_404(Usuarios, email=email)

    print(user.foto)
    return render(request, 'Paginas/Perfil.html', {'Usuarios': user})

def MeuAprendizado(request):
    if not request.session['login']:
        return redirect('landingPage')
    else:
        email = request.session['email']
        userID = Usuarios.objects.filter(email = email).first()

        if request.method != "POST":
            print(f'ID USUARIO: {userID}')

            cursos = Cursos.objects.filter(usuarioID=userID)
            user = get_object_or_404(Usuarios, email=email)
            fav = CursosFavorito.objects.filter(usuario=userID)

            for idx, curso in enumerate(cursos):
                videos = Video.objects.filter(cursoID=curso).count()
                cursos[idx].total_videos = videos
                aulas = AulaAssistida.objects.filter(curso=curso, usuario=user).count()
                cursos[idx].total_assistidos = aulas

            for i in fav:
                print(f'Favoritos: {i}')

            return render(request, 'Paginas/MeuAprendizado.html', {'Cursos': cursos, 'Usuarios': user, 'favorite': fav})

        else:
            idcurso = request.POST.get('btnFav')
            u = get_object_or_404(Usuarios, email=email)

            c = get_object_or_404(Cursos, id=idcurso)

            curso = CursosFavorito(usuario = u, curso = c)

            if CursosFavorito.objects.filter(usuario = u, curso = c).exists():
                CursosFavorito.objects.filter(usuario=u, curso=c).delete()
            else:
                CursosFavorito.save(curso)

            return redirect('MeuAprendizado')

def Catalogo(request):
    if not request.session['login']:
        return redirect('landingPage')

    curso = Cursos.objects.order_by('-id')
    paginator = Paginator(curso, 3)
    page = request.GET.get('p')
    curso = paginator.get_page(page)
    email = request.session['email']
    user = get_object_or_404(Usuarios, email=email)
    return render(request,  'Paginas/Catalogo.html', {'Cursos': curso, 'Usuarios': user})

def ComprarCurso(request, curso_id):
    if not request.session['login']:
        return redirect('landingPage')
    curso = get_object_or_404(Cursos, id=curso_id)
    videos = Video.objects.filter(cursoID=curso).count()
    curso.total_videos = videos

    if request.method != "POST":
        email = request.session['email']
        user = get_object_or_404(Usuarios, email=email)
        return render(request, 'Paginas/ComprarCurso.html', {'Cursos': curso, 'Usuarios': user})
    else:
        email = request.session['email']
        u1 = get_object_or_404(Usuarios, email=email)

        c1 = get_object_or_404(Cursos, id=curso_id)
        c1.usuarioID.add(u1)

        messages.add_message(request, messages.SUCCESS, 'Curso adquirido!')
        return render(request, 'Paginas/ComprarCurso.html', {'Cursos': curso, 'Usuarios': u1})

def PlayerVideo(request, curso_id):
    if not request.session['login']:
        return redirect('landingPage')

    curso = get_object_or_404(Cursos, id = curso_id)
    videos = Video.objects.filter(cursoID = curso_id)
    email = request.session['email']
    user = get_object_or_404(Usuarios, email=email)
    aulas = AulaAssistida.objects.filter(curso_id=curso_id, usuario=user).all()
    return render(
        request,
        'Paginas/PlayerVideo.html',
        {'Cursos': curso, 'Videos': videos, 'Usuarios': user, 'Aulas': aulas}
    )

def redefNome(request):
    if not request.session['login']:
        return redirect('landingPage')
    else:
        email = request.session['email']
        user = get_object_or_404(Usuarios, email=email)
        if request.method != 'POST':
            return render(request, 'Paginas/redefNome.html', {'Usuarios': user})
        else:
            nome = request.POST.get('nome')
            if nome == "" or nome == " ":
                pass
            else:
                Usuarios.objects.filter(email=email).update(nome=nome)

            return redirect('Perfil')

def redefDesc(request):
    if not request.session['login']:
        return redirect('landingPage')
    else:
        email = request.session['email']
        user = get_object_or_404(Usuarios, email=email)
        if request.method != 'POST':
            return render(request, 'Paginas/redefDesc.html', {'Usuarios': user})
        else:

            desc = request.POST.get('desc')
            if desc == "" or desc == " ":
                pass
            else:
                Usuarios.objects.filter(email=email).update(descricao = desc)

            return redirect('Perfil')

def redefPhoto(request):
    if not request.session['login']:
        return redirect('landingPage')
    else:
        email = request.session['email']
        if request.method != 'POST':
            return render(request, 'Paginas/redefPhoto.html')
        else:
            uploaded_file = request.FILES['asgnmnt_file']

            if uploaded_file:
                path = default_storage.save(
                    rf"fotos\2022\05\{uploaded_file}", ContentFile(uploaded_file.read()))
                os.path.join(settings.MEDIA_ROOT, path)

                Usuarios.objects.filter(email=email).update(foto=f'fotos/2022/05/{uploaded_file}')

            return redirect('Perfil')

# Páginas que podem ser acessadas sem estar logado
# Landing Page
def landingPage(request):
    request.session['login'] = False
    return render(request, 'Paginas/index.html')

# RedefinicaoSenha - RecuperacaoSenha
def Redefinicao(request):
    email = request.POST.get('email')

    if request.method != "POST":
        return render(request, 'Paginas/RedefinicaoSenha.html')
    else:
        if Usuarios.objects.filter(email = email).exists():
            request.session['EmailRedef'] = email
            return redirect('RecuperacaoSenha')
        else:
            messages.add_message(request, messages.ERROR, 'Email não existe')
            return render(request, 'Paginas/RedefinicaoSenha.html')

def Recuperacao(request):
    if request.method != "POST":
        return render(request, 'Paginas/RecuperacaoSenha.html')
    else:
        senha = request.POST.get('senha')
        email = request.session['EmailRedef']

        if len(senha) < 6:
            messages.add_message(request, messages.ERROR, 'Senha deve ser maior do que 6 caracteres')
            return render(request, 'Paginas/RecuperacaoSenha.html')
        else:
            senha = get_password_hash(senha)
            Usuarios.objects.filter(email = email).update(senha = senha)
            return redirect('index')

# Login
def index(request):
    request.session['login'] = False

    if request.method != "POST":
        return render(request, 'Paginas/Login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha = get_password_hash(senha)

        if not Usuarios.objects.filter(email = email, senha = senha):
            messages.add_message(request, messages.ERROR, 'Usuário ou senha incorretos')
            return render(request, 'Paginas/Login.html')
        else:
            nome = get_object_or_404(Usuarios, email=email)
            request.session['email'] = email
            request.session['nome'] = nome.nome
            request.session['login'] = True
            return redirect('Site_Educacional')

# Cadastro
def Cadastro(request):
    if request.method != 'POST':
        return render(request, 'Paginas/Cadastro.html')
    else:
        nomeGet = request.POST.get('nome')
        emailGet = request.POST.get('email')
        senhaGet = request.POST.get('senha')
        senha2Get = request.POST.get('senha2')

        if not nomeGet or not emailGet or not senhaGet or not senha2Get:
            messages.add_message(request, messages.ERROR, 'Nenhum campo pode ficar vazio')
            return render(request, 'Paginas/Cadastro.html')

        elif senhaGet != senha2Get:
            messages.add_message(request, messages.ERROR, 'Senhas devem ser iguais')
            return render(request, 'Paginas/Cadastro.html')

        elif len(senhaGet) < 6:
            messages.add_message(request, messages.ERROR, 'Senha deve ser maior que 6 caracteres')
            return render(request, 'Paginas/Cadastro.html')

        elif Usuarios.objects.filter(email = emailGet).exists():
            messages.add_message(request, messages.ERROR, 'Usuário já existe')
            return render(request, 'Paginas/Cadastro.html')
        try:
            validate_email(emailGet)
        except:
            messages.add_message(request, messages.ERROR, 'Email inválido')
            return render(request, 'Paginas/Cadastro.html')
        else:
            senhaGet = get_password_hash(senhaGet)
            user = Usuarios(nome= nomeGet, senha = senhaGet, email = emailGet)
            user.save()
            request.session['email'] = emailGet
            request.session['nome'] = nomeGet
            request.session['login'] = True
            return render(request, 'Paginas/Perfil.html', {'Usuarios': user})

# Não são paginas
# Encripta a senha
def get_password_hash(password: str) -> str:
    salt = b'1'  # Get the salt you stored for *this* user

    return str(pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        salt,
        100000
    ).hex())

def Logout(request):
    request.session['login'] = False
    return redirect('landingPage')

# Mecanismo de busca de cursos
def busca(request):
    termo = request.GET.get('termo')

    if str(termo) == "" or str(termo) == " ":
        return redirect('Catalogo')
    else:
        campos = Concat('nome', Value(' '))
        cursos = Cursos.objects.annotate(
            nome_curso=campos
        ).filter(
            Q(nome_curso__icontains=termo)
        )
        email = request.session['email']
        user = get_object_or_404(Usuarios, email=email)

        return render(request, 'Paginas/busca.html', {'Cursos': cursos, 'Usuarios': user})

def base(request):
    email = request.session['email']
    user = Usuarios.objects.filter(email=email)

    return {'Usuarios': user}

def theme(request):
    color = request.GET.get('color')
    email = request.session['email']

    if color == "Dark":
        Usuarios.objects.filter(email=email).update(userTheme = 2)
    else:
        Usuarios.objects.filter(email=email).update(userTheme = 1)

    return redirect('Site_Educacional')

def deletePhoto(request):
    email = request.session['email']
    Usuarios.objects.filter(email = email).update(foto = "")
    return redirect('Perfil')

def aula_assistida(request):
    id_aula = json.loads(request.body)['aula']
    id_curso = json.loads(request.body)['curso']
    email = request.session['email']

    usuario = Usuarios.objects.filter(email=email).first()
    video = Video.objects.filter(id=id_aula).first()
    curso = Cursos.objects.filter(id=id_curso).first()

    if not AulaAssistida.objects.filter(usuario=usuario, video=video, curso=curso).exists():
        aula = AulaAssistida(usuario=usuario, video=video, curso=curso, assistido=True)
        aula.save()

    return HttpResponse({'body': request.POST.get('aula')})
