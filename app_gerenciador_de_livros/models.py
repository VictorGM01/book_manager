from django.db import models


class StatusLivro(models.Model):
    status = models.TextField(max_length=10)

    def __str__(self):
        return self.status


class Generos(models.TextChoices):
    FICCAO = 'Ficção'
    NAO_FICCAO = 'Não-ficção'
    ACAO_E_AVENTURA = 'Ação e aventura'
    INFANTIL = 'Infantil'
    FICCAO_CRISTA = 'Ficção Cristã'
    CLASSICOS = 'Clássicos'
    QUADRINHOS = 'Quadrinhos'
    FICCAO_CONTEMP = 'Ficção Contemporânea'
    FANTASIA = 'Fantasia'
    FICCAO_HISTORICA = 'Ficção Histórica'
    FICCAO_LITERARIA = 'Ficção Literária'
    MISTERIO = 'Mistério e Crime'
    PECAS_ROTEIROS = 'Peças e Roteiros'
    POESIA = 'Poesia'
    ROMANCE = 'Romance'
    ROMANCE_CONTEMP = 'Romance contemporâneo'
    ROMANCE_HISTORICO = 'Romance histórico'
    ROMANCE_POLICIAL = 'Romance Policial'
    SUSPENSE_ROMANTICO = 'Suspense Romântico'
    FICCAO_CIENTIFICA = 'Ficção Científica'
    CONTOS = 'Contos'
    SUSPENSE = 'Suspense'
    HORROR = 'Horror'
    BIOGRAFIA = 'Biografias e Memórias'
    JOVEM_ADULTO = 'Jovem-Adulto'
    INFANTO_JUVENIL = 'Infanto-Juvenil'
    AUTOBIO = 'Autobiografia'
    TECNOLOGIA = 'Tecnologia'
    CULINARIA = 'Culinária'
    EDUCACAO = 'Educação'
    SAUDE = 'Saúde e Bem-estar'
    ARTE = 'Arte'
    HISTORIA = 'História'
    LEI = 'Lei'
    MUSICA = 'Música'
    FILOSOFIA = 'Filosofia'
    PSICOLOGIA = 'Psicologia'
    SOCIOLOGIA = 'Sociologia'
    MATEMATICA = 'Matemática'
    RELIGIAO = 'Religião e Espiritualidade'
    AUTOAJUDA = 'Autoajuda'
    ESPORTES = 'Esportes'
    CRIME_VERDADEIRO = 'Crime Verdadeiro'
    ROMANCE_SOBRENATURAL = 'Romance Sobrenatural'
    CHICK_LIT = 'Chick-Lit'
    EPICO = 'Épico/Aventura'
    DISTOPIA = 'Distopia'
    SICK_LIT = 'Sick-Lit'



class Livros(models.Model):
    nome_do_livro = models.CharField(max_length=200)
    editora_do_livro = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    generos = models.TextField(max_length=50, choices=Generos.choices)
    situacao = models.ForeignKey(StatusLivro, on_delete=models.CASCADE)
    estrelas = models.IntegerField(blank=True, null=True)
    opiniao = models.TextField(max_length=500, blank=True)
    foto_do_livro = models.ImageField(upload_to='imagens/%d/%m', blank=True)
