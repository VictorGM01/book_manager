from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_gerenciador_de_livros.urls')),
    path('admin/', admin.site.urls)
]
