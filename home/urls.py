"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home_page.views import index_home
from dashboard.views import index_dashboard
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [

    # Rota para a página administrativa
    path('admin/', admin.site.urls),

    # Rotas para a página Home - Inicial
    path('index/', index_home.index),
    path('resumo/', index_home.resumo),
    path('formacao_cursos_complementares_home/', index_home.formacao_cursos_complementares_home),
    path('formacao_academica_home/', index_home.formacao_academica_home),
    path('contatos/', index_home.contatos_home),


    # Rotas para a Dashboard
    path('dashboard/index/', index_dashboard.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
