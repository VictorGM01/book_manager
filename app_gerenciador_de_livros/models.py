from django.db import models


class StatusLivro(models.Model):
    status = models.TextField(max_length=10)

    def __str__(self):
        return self.status


class Livros(models.Model):
    nome_do_livro = models.CharField(max_length=200)
    editora_do_livro = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    generos = models.CharField(max_length=200)
    situacao = models.ForeignKey(StatusLivro, on_delete=models.CASCADE)
    estrelas = models.IntegerField(blank=True, null=True)
    opiniao = models.TextField(max_length=500, blank=True)
    foto_do_livro = models.ImageField(upload_to='imagens/%d/%m', blank=True)
