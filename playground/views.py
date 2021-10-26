from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, OrderItem


from django.db.models import Q, F

def say_hello(request):
    query_set = Product.objects.filter(inventory=F('collection__id'))


    context = {"name": "Olamide", "products": list()}
    return render(request, 'hello.htm', {"products": query_set})
