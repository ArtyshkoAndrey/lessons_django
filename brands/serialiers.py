from products.models import Product
from rest_framework import serializers
from .models import Brand


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', 'products')
