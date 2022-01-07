from django.db import models


class Livros(models.Model):
    nome_do_livro = models.CharField(max_length=200)
    editora_do_livro = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    estrelas = models.IntegerField()
    situacao = models.CharField(blank=True)
    opiniao = models.TextField(blank=True)
