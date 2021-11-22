from django.shortcuts import render
import requests
from home.settings import base

# Create your views here.



def index(request):
    return render(request, 'index_home.html')

def resumo(request):
    db = requests.get(base.URL_API_ENV)
    aux = db.json()
    i = 0
    for dt in aux:
        year = aux[i]['start_date']
        aux[i]['start_date'] = year[0:4]

        year = aux[i]['departure_date']
        aux[i]['departure_date'] = year[0:4]
        i = i+1

    context = {
        'dts': aux,
    }
    print(type(db))
    return render(request,'resumo_home.html', context)

def formacao_cursos_complementares_home(request):
    return render(request,'formacao_cursos_complementares_home.html')

def formacao_academica_home(request):
    return render(request,'formacao_academica_home.html')

def contatos_home(request):
    return render(request,'contatos_home.html')
