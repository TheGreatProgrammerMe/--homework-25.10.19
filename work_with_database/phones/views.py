from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    my_request = request.GET.get('sort')
    object_count = Phone.objects.last().id
    if str(my_request) == 'name':
        objects = Phone.objects.all().filter().order_by('name')
    elif str(my_request) == 'min_price':
        objects = Phone.objects.all().filter().order_by('price')
    elif str(my_request) == 'max_price':
        objects = Phone.objects.all().filter().order_by('-price')
    else:
        objects = Phone.objects.all()
    
    context = {
    'objects': objects,
    'ides': [i for i in range(object_count)],
    'href_name': '/catalog?sort=name',
    'href_min_price': '/catalog?sort=min_price',
    'href_max_price': '/catalog?sort=max_price'
    }

    return render(request, template, context)
    

def show_product(request, slug):
    template = 'product.html'
    obj = Phone.objects.get(slug=slug)
    context = {
    'name' : obj.name,
    'image' : obj.image,
    'price' : obj.price,
    'release_date' : obj.release_date,
    'lte_exists' : obj.lte_exists
    }
    return render(request, template, context)
