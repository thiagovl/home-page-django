from django.shortcuts import render
import requests
from home.settings import base

# Create your views here.

def index(request):
    return render(request, 'index_home.html')

def professional_experience(request):
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
    return render(request,'professional_experience_home.html', context)

def formacao_cursos_complementares_home(request):
    return render(request,'complementary_courses_home.html')

def formacao_academica_home(request):
    return render(request,'academic_education_home.html')

def contatos_home(request):
    return render(request,'contacts_home.html')
