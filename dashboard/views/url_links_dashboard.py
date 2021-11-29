from django.shortcuts import render, redirect
import requests

from home.settings import base

def register_url_links(request):
    return render(request, 'register_url_links.html')

def register_url_links_add(request):
    dt = {
        'id' : None,
        'name' : request.POST.get('name'),
        'url_name' : request.POST.get('url_name'),
        'briefsummary' : request.POST.get('briefsummary'),
        'tags' : request.POST.get('tags'),
        'favorites' : request.POST.get('favorites'),
        'date_created' : request.POST.get('date_created')
    }
    r = requests.post(base.URL_API_URL_TRUE, dt)
    return redirect('/dashboard/register_url/')