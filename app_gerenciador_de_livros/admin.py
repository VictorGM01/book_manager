from django.contrib import admin
from .models import Livros


class ListaLivros(admin.ModelAdmin):
    list_display = ('nome_do_livro', 'autor', 'estrelas', 'editora_do_livro', 'id')
    list_display_links = ('nome_do_livro', 'id')
    search_fields = ('nome_do_livro', 'generos', 'autor')
    list_filter = ('estrelas', 'autor', 'editora_do_livro')
    list_per_page = 10

    def get_queryset(self, request):
        qs = super(ListaLivros, self).get_queryset(request)
        return qs.order_by('nome_do_livro')


# Registra banco de dados à página do admin
admin.site.register(Livros, ListaLivros)
