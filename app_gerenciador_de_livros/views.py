from django.shortcuts import render, get_object_or_404, redirect
from .models import Livros


def index(request):
    """Página Principal da Aplicação"""
    livros = Livros.objects.order_by('nome_do_livro').all()

    dados = {
        'livros': livros
    }

    return render(request, 'index.html', dados)


def buscar(request):
    """Página de busca"""
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
    """Página que contém as informações do livro"""
    livro_a_exibir = get_object_or_404(Livros, pk=id_livro)

    sugestoes = Livros.objects.filter(generos__icontains=livro_a_exibir.generos).exclude(id=id_livro)[:3]

    dados = {
        'livro': livro_a_exibir,
        'sugestoes': sugestoes
    }

    return render(request, 'livro.html', dados)


def marcar_como_lido(request, id_livro):
    """Responsável por mudar a situação do livro para 'lido'"""
    livro_a_mudar = get_object_or_404(Livros, pk=id_livro)
    livro_a_mudar.situacao_id = 1
    livro_a_mudar.save()
    return redirect(f'/{id_livro}')


def adiciona_livro(request):
    """Adiciona novo livro ao banco de dados"""
    global situacao_id
    if request.method == 'POST':
        nome = request.POST['nome_livro']
        editora = request.POST['editora_livro']
        autor = request.POST['autor_livro']
        genero = request.POST['genero_livro']
        situacao = request.POST['situacao']
        estrelas = request.POST['estrelas']
        opiniao = request.POST['opiniao']
        foto = request.FILES.get('foto_livro')

        if not nome.strip() or not editora.strip() or not autor.strip() or not genero.strip() or not situacao.strip():
            return redirect('add_livro')

        if situacao == 'Lido':
            situacao_id = 1

        elif situacao == 'Não Lido':
            situacao_id = 2

        elif situacao == 'Lendo':
            situacao_id = 3

        if estrelas == '':
            estrelas = None

        novo_livro = Livros.objects.create(nome_do_livro=nome, editora_do_livro=editora, autor=autor, generos=genero,
                                           situacao_id=situacao_id, estrelas=estrelas, opiniao=opiniao,
                                           foto_do_livro=foto)
        novo_livro.save()

        return redirect('index')

    return render(request, 'adiciona_livro.html')


def edita_livro(request, id_livro):
    """Edita informações de um livro já cadastrado"""
    livro_selecionado = get_object_or_404(Livros, pk=id_livro)
    livro_a_editar = {
        'livro': livro_selecionado
    }

    return render(request, 'edita_livro.html', livro_a_editar)


def atualiza_livro(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']

        livro_a_editar = Livros.objects.get(pk=livro_id)

        livro_a_editar.nome_do_livro = request.POST['nome_livro']
        livro_a_editar.editora_do_livro = request.POST['editora_livro']
        livro_a_editar.autor = request.POST['autor_livro']
        livro_a_editar.generos = request.POST['genero_livro']
        livro_a_editar.situacao = request.POST['situacao']
        livro_a_editar.estrelas = request.POST['estrelas']
        livro_a_editar.opiniao = request.POST['opiniao']
        if 'foto_livro' in request.FILES:
            livro_a_editar.foto_do_livro = request.FILES['foto_livro']
