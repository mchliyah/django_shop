from django.http import HttpResponse
from .models import Products
from django.shortcuts import render

# need mapping in the urls folder


def index(request):
    product = Products.objects.all()
    return render(request, 'index.html', {'product': product})


def test(request):
    return HttpResponse('this is a test for now !!!!')

