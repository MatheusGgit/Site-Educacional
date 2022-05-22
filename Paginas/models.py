from django.db import models
from django.utils import timezone

class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')
    objects = models.Manager()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    categoriaCurso = models.CharField(max_length = 55)


    def __str__(self):
        return self.categoriaCurso

class Cursos(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=444, blank=True)
    aulas = models.IntegerField()
    fonte = models.CharField(max_length=255)
    linkFonte = models.CharField(max_length=400)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y')
    horas = models.TimeField()
    objects = models.Manager()
    usuarioID = models.ManyToManyField(Usuarios, blank=True)
    categoriaID = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=4)

    def __str__(self):
        return self.nome

class Video(models.Model):
    nomeAula = models.CharField(max_length=255)
    video = models.FileField(upload_to=f'videos/%Y')
    cursoID = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.nomeAula

