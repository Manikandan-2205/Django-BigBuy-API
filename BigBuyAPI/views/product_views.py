from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from BigBuyAPI.models.product import Product, ProductCategory,ProductDetails
from BigBuyAPI.models.brand import Brand
from BigBuyAPI.models.productstack import ProductStack

from BigBuyAPI.serializers.product_serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    BrandSerializer,    
    ProductDetailsSerializer,
    ProductStackSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_description="Retrieve all products",
        responses={200: ProductSerializer(many=True)},
    )
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={200: ProductSerializer()},
    )
    def retrieve(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={201: ProductSerializer()},
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a product by ID",
        request_body=ProductSerializer,
        responses={200: ProductSerializer()},
    )
    def update(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a product by ID", responses={204: "No Content"}
    )
    def destroy(self, request, pk=None):
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    Department Master Details
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    @swagger_auto_schema(
        operation_description="Department Master Details",
        request_body=ProductCategorySerializer,
        responses={201: ProductCategorySerializer()},
    )
    def Department(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailsViewSet(viewsets.ModelViewSet):
    """
    Department Master Details
    """

    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer

    @swagger_auto_schema(
        operation_description="Department Master Details",
        request_body=ProductDetailsSerializer,
        responses={201: ProductDetailsSerializer()},
    )
    def Department(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class BrandViewSet(viewsets.ModelViewSet):
    """
    Department Master Details
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @swagger_auto_schema(
        operation_description="Department Master Details",
        request_body=BrandSerializer,
        responses={201: BrandSerializer()},
    )
    def Department(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class ProductStackViewSet(viewsets.ModelViewSet):
    """
    Department Master Details
    """

    queryset = ProductStack.objects.all()
    serializer_class = ProductStackSerializer

    @swagger_auto_schema(
        operation_description="Department Master Details",
        request_body=ProductStackSerializer,
        responses={201: ProductStackSerializer()},
    )
    def Department(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
