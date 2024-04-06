from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    query_selector = Product.objects.all()





    kaka=2
    dhola = 22





    return render(request, 'hello.html', {'name': 'Mosh'})
