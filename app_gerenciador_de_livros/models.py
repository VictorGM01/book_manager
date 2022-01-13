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
    estrelas = models.IntegerField(blank=True, null=True)
    opiniao = models.TextField(max_length=500, blank=True)
