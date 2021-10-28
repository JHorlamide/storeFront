from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, OrderItem



def say_hello(request):
    product = Product.objects.latest('unit_price')


    # return render(request, 'hello.htm', {"products": list(query_set)})
    return render(request, 'hello.htm', {"product": product})
