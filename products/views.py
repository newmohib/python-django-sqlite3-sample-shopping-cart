from django.http import HttpResponse
from django.shortcuts import render
from .models import  Product


# package.model / method

# Create your views here.

# /products -> index
# Uniform Resource Locator ( Address )

def index(request):
    products = Product.objects.all()
    # filter(), save(), get()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')
