# Generated by Django 4.0.1 on 2022-01-11 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gerenciador_de_livros', '0006_alter_livros_estrelas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'ordering': ['nome_do_livro']},
        ),
    ]