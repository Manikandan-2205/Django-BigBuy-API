from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from BigBuyAPI.models.order import Order
from BigBuyAPI.models.ordertransaction import OrderTransaction
from BigBuyAPI.serializers.order_serializers import OrderSerializer, OrderTransactionSerializer
from BigBuyAPI.models.product import Product
from BigBuyAPI.serializers.product_serializers import ProductSerializer



class OrderViewSet(viewsets.ModelViewSet):
    """
    Order API with Swagger Documentation
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @swagger_auto_schema(
        operation_description="Retrieve all orders",
        responses={200: OrderSerializer(many=True)},
    )
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve an order by ID",
        responses={200: OrderSerializer()},
    )
    def retrieve(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new order",
        request_body=OrderSerializer,
        responses={201: OrderSerializer()},
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update an order by ID",
        request_body=OrderSerializer,
        responses={200: OrderSerializer()},
    )
    def update(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an order by ID", responses={204: "No Content"}
    )
    def destroy(self, request, pk=None):
        order = self.get_object()
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderTransactionViewSet(viewsets.ModelViewSet):
    """
    Department Master Details
    """

    queryset = OrderTransaction.objects.all()
    serializer_class = OrderTransactionSerializer

    @swagger_auto_schema(
        operation_description="Department Master Details",
        request_body=OrderTransactionSerializer,
        responses={201: OrderTransactionSerializer()},
    )
    def Department(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
