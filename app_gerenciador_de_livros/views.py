from django.shortcuts import render
from .models import Livros


def index(request):
    livros = Livros.objects.all()

    dados = {
        'livros': livros
    }

    return render(request, 'index.html', dados)
