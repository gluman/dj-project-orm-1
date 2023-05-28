from django.shortcuts import render
from app.models import Phone

# Create your views here.

def index(request):
    context = {
        'title': 'Main page',
        'body': 'Hello',
    }
    return render(request, 'base.html', context)

def phones_catalog(request, phone='None'):
    orderby = request.GET.get('sort', 'name')

    if orderby == 'min_price':
        sort = 'price'
    elif orderby =='max_price':
        sort = '-price'
    elif orderby == 'name':
        sort = 'name'


    if phone == 'None':
        template = 'catalog.html'
        phone_objects = Phone.objects.all().order_by(sort)
    else:
        template = 'product.html'
        phone_objects = Phone.objects.filter(slug=phone).order_by(sort)

    phones = []
    for p in phone_objects:
        phones.append({'name': p.name,
                       'price': p.price,
                       'image': p.image,
                       'release_date': p.release_date,
                       'lte_exists': p.lte_exists,
                       'slug': p.slug
                       })
    context = {'phones': phones}

    return render(request, template, context)
