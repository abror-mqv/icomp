from django.http import request
from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView
# Create your views here.

def index(request):
    products = Product.objects.order_by('-id')
    products = products[0], products[1], products[2]
    return render(request, 'main/index.html', {'products': products})

class DView(DetailView):
    model = Product
    template_name = 'main/dview.html'
    context_object_name = 'laptop'

def catalog(request):
    products = Product.objects.order_by('-price')
    return render(request, 'main/catalog.html', {'products': products})

def aboutus(request):
    return render(request, 'main/about-us.html')