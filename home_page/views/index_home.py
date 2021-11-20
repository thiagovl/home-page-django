from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index_home.html')

def resumo(request):
    return render(request,'resumo_home.html')

def formacao_cursos_complementares_home(request):
    return render(request,'formacao_cursos_complementares_home.html')

def formacao_academica_home(request):
    return render(request,'formacao_academica_home.html')

def contatos_home(request):
    return render(request,'contatos_home.html')
