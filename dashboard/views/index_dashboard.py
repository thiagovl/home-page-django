from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index_dashboard.html')

def register_url_links(request):
    return render(request, 'register_url_links.html')

