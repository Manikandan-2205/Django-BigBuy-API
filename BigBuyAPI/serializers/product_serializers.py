# BigBuyAPI/serializers/product_serializers.py

from rest_framework import serializers
from BigBuyAPI.models.product import Product, ProductCategory, Brand, ProductDetails
from BigBuyAPI.models.productstack import ProductStack 

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'

class ProductStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStack
        fields = '__all__'