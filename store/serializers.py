from decimal import Decimal

from rest_framework import serializers

from .models import Product, Collection

# Field Types for serializing relationships.

# 1: Nested Object
# collection = CollectionSerializer()

# 2: PrimaryKeyRelatedField
# collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

# 3: StringRelatedField
# Django will convert each collection to an object and return it here.
# collection = serializers.StringRelatedField()

# 4: Hyperlink


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']

    product_count = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug',  'inventory',
                  'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
