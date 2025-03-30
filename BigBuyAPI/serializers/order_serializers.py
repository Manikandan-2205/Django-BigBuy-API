from rest_framework import serializers
from BigBuyAPI.models.order import Order
from BigBuyAPI.models.ordertransaction import OrderTransaction

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTransaction
        fields = '__all__'
