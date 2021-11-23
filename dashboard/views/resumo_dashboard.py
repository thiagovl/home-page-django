from django.shortcuts import render, redirect
import requests
from home.settings import base

def insert_experience_view(request):
    return render(request, 'register_experience_dashboard.html')

def insert_resumo(request):
    dt = {
        'id' : None,
        'company' : request.POST.get('company'),
        'occupation' : request.POST.get('occupation'),
        'briefsummary' : request.POST.get('briefsummary'),
        'activities' : request.POST.get('activities'),
        'tags' : request.POST.get('tags'),
        'start_date' : request.POST.get('start_date'),
        'departure_date' : request.POST.get('departure_date')
    }
    r = requests.post(base.URL_API_ENV, dt)
    return redirect('/dashboard/experience/')
