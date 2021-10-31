from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist

# from store.models import Product, OrderItem

from store.models import Product, OrderItem

def say_hello(request):
    queryset = OrderItem.objects.all()

    return render(request, 'hello.htm', {"products": list(queryset)})
