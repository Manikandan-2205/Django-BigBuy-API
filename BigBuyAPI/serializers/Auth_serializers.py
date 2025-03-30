from rest_framework import serializers
from BigBuyAPI.models.jwttoken import Jwttoken,UserLog

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jwttoken
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = '__all__'
