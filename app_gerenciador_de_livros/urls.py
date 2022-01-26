from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('<int:id_livro>', views.livro, name='livro'),
    path('marcar-como-lido/<int:id_livro>', views.marcar_como_lido, name='marcar_como_lido'),
    path('adiciona/livro', views.adiciona_livro, name='add_livro'),
    path('edita/<int:id_livro>', views.edita_livro, name='edita_livro'),
    path('atualiza_livro', views.atualiza_livro, name='atualiza_livro')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
