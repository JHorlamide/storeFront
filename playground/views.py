from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, OrderItem


def say_hello(request):
    query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20)) # & => AND

    query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20)) # | => OR



    context = {"name": "Olamide", "products": list()}
    return render(request, 'hello.htm', {"products": query_set})
