import csv

from django.shortcuts import render

# Create your views here.

def read_csv():
    with open('phones.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
           phone = Phone()

def index(request):
    return render(request, 'base.html')

def phones_catalog(request, phone):

    context = {}
    return render(request, 'catalog.html', context)
