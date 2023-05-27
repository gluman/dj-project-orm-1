from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html')

def phones_catalog(request, phone):


    context = {}
    return render(request, 'catalog.html', context)
