from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, OrderItem


def say_hello(request):
    query_set = Product.objects.filter(description__isnull=True)



    context = {"name": "Olamide", "products": list()}
    return render(request, 'hello.htm', context)
