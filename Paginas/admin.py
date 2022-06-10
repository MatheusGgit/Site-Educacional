from django.contrib import admin
from .models import Cursos, Usuarios, Video, Categoria, Theme, CursosFavorito, AulaAssistida

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'data_criacao')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    search_fields = ('nome', 'email')
    list_editable = ('email', )

admin.site.register(Cursos)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Video)
admin.site.register(Categoria)
admin.site.register(Theme)
admin.site.register(CursosFavorito)
admin.site.register(AulaAssistida)