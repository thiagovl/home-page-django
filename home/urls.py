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
from home_page.views import index_home, views_home, views_login
from dashboard.views import index_dashboard, resumo_dashboard, url_links_dashboard
from django.conf import settings  
from django.conf.urls.static import static  
from django.conf.urls import include, url

urlpatterns = [

    # Rota para a página administrativa
    path('admin/', admin.site.urls),    

    # Rotas para a página Home - Inicial
    path('', index_home.index),
    path('experience/', index_home.professional_experience),
    path('complementary_courses_home/', index_home.formacao_cursos_complementares_home),
    path('academic_education_home/', index_home.formacao_academica_home),
    path('contacts/', index_home.contatos_home),

    # Rotas para as views
    path('view/experience/<id>/', views_home.view_professional_experience_home),
    path('view/login/', views_login.views_singup),

    # Rotas para a Dashboard
    path('dashboard/', index_dashboard.index),
    path('dashboard/experience/', resumo_dashboard.insert_experience_view),
    path('dashboard/experience/add', resumo_dashboard.insert_resumo),
    path('dashboard/register_url/', url_links_dashboard.register_url_links),
    path('dashboard/register_url/add', url_links_dashboard.register_url_links_add),

    # Rotas para funções diversas
    path('view/login', views_login.singup),
    path('logout/', views_login.logout_user),

    url('avatars/', include('avatar.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
