import csv

from django.shortcuts import render


# Create your views here.




def index(request):
    context = {
        'title': 'Main page',
        'body': 'Hello',
    }
    return render(request, 'base.html', context)

def phones_catalog(request, phone):

    context = {}
    return render(request, 'catalog.html', context)
