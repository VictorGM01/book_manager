from django.contrib import admin
from .models import Livros


class ListaLivros(admin.ModelAdmin):
    list_display = ('nome_do_livro', 'autor', 'estrelas', 'editora_do_livro', 'situacao', 'id')
    list_display_links = ('nome_do_livro', 'id')
    search_fields = ('nome_do_livro', 'generos')
    list_filter = ('autor', 'estrelas', 'editora_do_livro', 'generos', 'situacao')
    list_per_page = 10


# Registra banco de dados à página do admin
admin.site.register(Livros, ListaLivros)
