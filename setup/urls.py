"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index, entrar, cadastrar, sair, adicionar_evento, informacoes_evento, editar_evento, excluir_evento, adicionar_equipe, informacoes_equipe, editar_equipe, informacoes_round, excluir_round, excluir_equipe, visao_geral_evento
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('entrar/', entrar, name='entrar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('sair/', sair, name='sair'),

    path('adicionar_evento/', adicionar_evento, name='adicionar_evento'),
    path('informacoes_evento/<int:id>/', informacoes_evento, name='informacoes_evento'),
    path('editar_evento/<int:id>/', editar_evento, name='editar_evento'),
    path('excluir_evento/<int:id>/', excluir_evento, name='excluir_evento'),

    path('adicionar_equipe/<int:id>/', adicionar_equipe, name='adicionar_equipe'),
    path('excluir_equipe/<int:id>/', excluir_equipe, name='excluir_equipe'),
    path('informacoes_equipe/<int:id>/', informacoes_equipe, name='informacoes_equipe'),
    path('editar_equipe/<int:id>/', editar_equipe, name='editar_equipe'),

    path('informacoes_round/<int:id>/', informacoes_round, name='informacoes_round'),
    path('excluir_round/<int:id>/', excluir_round, name='excluir_round'),

    path('visao_geral_evento/<int:id>/', visao_geral_evento, name='visao_geral_evento'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
