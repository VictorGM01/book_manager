from django.shortcuts import render, get_object_or_404, redirect
from .models import Livros


def index(request):
    livros = Livros.objects.order_by('nome_do_livro').all()

    dados = {
        'livros': livros
    }

    return render(request, 'index.html', dados)


def buscar(request):
    lista_livros = Livros.objects.all()

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']

        if buscar:
            lista_livros = lista_livros.filter(nome_do_livro__icontains=nome_a_buscar)

    dados = {
        'livros': lista_livros
    }

    return render(request, 'buscar.html', dados)


def livro(request, id_livro):

    livro_a_exibir = get_object_or_404(Livros, pk=id_livro)

    sugestoes = Livros.objects.filter(generos__icontains=livro_a_exibir.generos).exclude(id=id_livro)[:3]

    dados = {
        'livro': livro_a_exibir,
        'sugestoes': sugestoes
    }

    return render(request, 'livro.html', dados)


def marcar_como_lido(request, id_livro):
    livro_a_mudar = get_object_or_404(Livros, pk=id_livro)
    livro_a_mudar.situacao_id = 1
    livro_a_mudar.save()
    return redirect(f'/{id_livro}')


def adiciona_livro(request):
    global situacao_id
    if request.method == 'POST':
        nome = request.POST['nome_livro']
        editora = request.POST['editora_livro']
        autor = request.POST['autor_livro']
        genero = request.POST['genero_livro']
        situacao = request.POST['situacao']
        estrelas = request.POST['estrelas']
        opiniao = request.POST['opiniao']
        foto = request.FILES['foto_livro']

        if not nome.strip() or not editora.strip() or not autor.strip() or not genero.strip() or not situacao.strip():
            return redirect('add_livro')

        if situacao == 'Lido':
            situacao_id = 1

        elif situacao == 'Não Lido':
            situacao_id = 2

        elif situacao == 'Lendo':
            situacao_id = 3

        novo_livro = Livros.objects.create(nome_do_livro=nome, editora_do_livro=editora, autor=autor, generos=genero,
                                           situacao_id=situacao_id, estrelas=estrelas, opiniao=opiniao,
                                           foto_do_livro=foto)

        novo_livro.save()

        return redirect('index')

    return render(request, 'adiciona_livro.html')
