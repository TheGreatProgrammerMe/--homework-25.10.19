from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    my_request = request.GET.get('sort')
    object_count = Phone.objects.last().id
    if str(my_request) == 'name':
        ides = [(Phone.objects.all().filter().order_by('name')[i].id-1) for i in range(object_count)]
    elif str(my_request) == 'min_price':
        ides = [(Phone.objects.all().filter().order_by('price')[i].id-1) for i in range(object_count)]
    elif str(my_request) == 'max_price':
        ides = [(Phone.objects.all().filter().order_by('-price')[i].id-1) for i in range(object_count)]
    else:
        ides = [i for i in range(object_count)]
    print(ides)
    
    context = {
    'ides': ides,
    'name' : [Phone.objects.filter()[i].name for i in range(object_count)],
    'image' : [Phone.objects.filter()[i].image for i in range(object_count)],
    'price' : [Phone.objects.filter()[i].price for i in range(object_count)],
    'slug' : [Phone.objects.filter()[i].slug for i in range(object_count)],
    'object_count': object_count,
    'href_name': '/catalog?sort=name',
    'href_min_price': '/catalog?sort=min_price',
    'href_max_price': '/catalog?sort=max_price'
    }

    return render(request, template, context)
    

def show_product(request, slug):
    template = 'product.html'
    obj = Phone.objects.get(slug='/catalog/'+slug)
    context = {
    'name' : obj.name,
    'image' : obj.image,
    'price' : obj.price,
    'release_date' : obj.release_date,
    'lte_exists' : obj.lte_exists
    }
    return render(request, template, context)
