# Generated by Django 4.0.1 on 2022-01-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gerenciador_de_livros', '0003_alter_livros_estrelas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='estrelas',
            field=models.IntegerField(),
        ),
    ]
