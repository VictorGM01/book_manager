from django.shortcuts import render
from .models import Livros


def index(request):
    livros = Livros.objects.order_by('nome_do_livro')

    dados = {
        'livros': livros
    }

    return render(request, 'index.html', dados)
