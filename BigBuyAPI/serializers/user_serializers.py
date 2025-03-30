from rest_framework import serializers
from BigBuyAPI.models.user import User
from BigBuyAPI.models.useraddress import UserAddress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"
