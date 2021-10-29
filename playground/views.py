from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist

# from store.models import Product, OrderItem

from store.models import Product, OrderItem

def say_hello(request):
    # Solution: 1
    ordered_items = OrderItem.objects.values_list('product__id').distinct()
    queryset = Product.objects.filter(id__in=ordered_items).order_by('title')

    # Solution: 2
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values_list('product__id')).order_by('title')

    return render(request, 'hello.htm', {"products": list(queryset)})
