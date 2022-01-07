from django.contrib import admin
from .models import Livros

# Registra banco de dados à página do admin
admin.site.register(Livros)
