from abc import ABC
from decimal import Decimal
from rest_framework import serializers

from .models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )

    # Nested Object
    # collection = CollectionSerializer()

    # Field Types for serializing relationship.

    # PrimaryKeyRelatedField
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    # StringRelatedField
    # Django will convert each collection to an object and return it here.
    # collection = serializers.StringRelatedField()

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
