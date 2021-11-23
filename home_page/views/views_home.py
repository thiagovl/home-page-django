from django.shortcuts import render
import requests
from home.settings import base


def view_professional_experience_home(request, id):
    db = requests.get(base.URL_API_ENV + id)
    aux = db.json()
    acts = aux['activities'].split('\n')
    context = {
        'dts': aux,
        'acts': acts
    }
    return render(request, 'view_professional_experience_home.html', context)