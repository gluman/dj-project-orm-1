import csv

from django.shortcuts import render

from app.models import Phone
# Create your views here.

def slugging(text):
    text_list = text.lower().split(' ')
    slug = '-'.join(text_list)
    return slug
def read_csv():
    phones = Phone()

    with open('phones.csv', 'rb') as f:
        line_count = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if line_count == 0:
               line_count += 1
               continue
            else:
                phone = Phone(
                    name=row[1],
                    image=row[2],
                    price=row[3],
                    release_date=row[4],
                    lte_exists=row[5],
                    slug=slugging(row[1]),
                )
                phone.save()
                line_count += 1

def index(request):
    return render(request, 'base.html')

def phones_catalog(request, phone):

    context = {}
    return render(request, 'catalog.html', context)
