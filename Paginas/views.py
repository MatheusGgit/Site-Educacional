from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.validators import validate_email
from django.contrib import messages
from .services.auth import Authentication
from .services.redefinicao_email_auth import Authentication_email, Email_Redef
from .services.cursosAuth import userCursos
from hashlib import *
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Usuarios, Cursos, Video


# Páginas - não é possível acessar sem estar logado
def Site_Educacional(request):
    if not request.session['login']:
        return redirect('landingPage')
    email = request.session['email']
    user = get_object_or_404(Usuarios, email=email)
    curso = get_object_or_404(Cursos, id = 1)
    curso2 = get_object_or_404(Cursos, id = 2)
    curso3 = get_object_or_404(Cursos, id = 3)
    return render(request, 'Paginas/Site_Educacional.html', {'Usuarios': user, 'Cursos': curso,
                                                             'Cursos2': curso2, 'Cursos3': curso3})

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

    email = request.session['email']
    userID = userCursos().email_get(email)
    print(f'ID USUARIO: {userID}')

    curso = Cursos.objects.filter(usuarioID = userID)
    user = get_object_or_404(Usuarios, email=email)

    # return render_to_response('index.html', {'user': Usuarios.objects.all()}, context_instance=RequestContext(request))
    return render(request, 'Paginas/MeuAprendizado.html', {'Cursos': curso, 'Usuarios': user})

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

    if request.method != "POST":
        email = request.session['email']
        user = get_object_or_404(Usuarios, email=email)
        return render(request, 'Paginas/ComprarCurso.html', {'Cursos': curso, 'Usuarios': user})
    else:
        email = request.session['email']
        u1 = get_object_or_404(Usuarios, email=email)

        c1 = get_object_or_404(Cursos, id=curso_id)
        c1.usuarioID.add(u1)
        messages.add_message(request, messages.SUCCESS, 'Curso Adquirido!')
        return render(request, 'Paginas/ComprarCurso.html', {'Cursos': curso, 'Usuarios': u1})

def PlayerVideo(request, curso_id):
    if not request.session['login']:
        return redirect('landingPage')

    curso = get_object_or_404(Cursos, id = curso_id)
    videos = Video.objects.filter(cursoID = curso_id)
    email = request.session['email']
    user = get_object_or_404(Usuarios, email=email)
    return render(request, 'Paginas/PlayerVideo.html', {'Cursos': curso, 'Videos': videos, 'Usuarios': user})

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
            user = Usuarios.objects.filter(email = email).update(foto = f'fotos/2022/05/{uploaded_file}')
            return redirect('Perfil')


# Páginas que podem ser acessadas sem estar logado
# Landing Page
def landingPage(request):
    request.session['login'] = False
    return render(request, 'Paginas/landingPage.html')

# RedefinicaoSenha - RecuperacaoSenha
def Redefinicao(request):
    email = request.POST.get('email')

    if request.method != "POST":
        return render(request, 'Paginas/RedefinicaoSenha.html')
    else:
        if Authentication_email().email_get(email):
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
        senha2 = request.POST.get('senha2')
        email = request.session['EmailRedef']

        if Email_Redef().email_redef(senha, senha2, email):
            if len(senha) < 6:
                messages.add_message(request, messages.ERROR, 'Senha deve ser maior do que 6 caracteres')
                return render(request, 'Paginas/RecuperacaoSenha.html')
            else:
                return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Senhas devem ser iguais')
            return render(request, 'Paginas/RecuperacaoSenha.html')

# Login
def index(request):
    request.session['login'] = False

    if request.method != "POST":
        return render(request, 'Paginas/Login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not Authentication().login(email, senha):
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

    return redirect('index')

