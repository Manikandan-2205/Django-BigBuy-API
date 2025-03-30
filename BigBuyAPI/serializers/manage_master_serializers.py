from rest_framework import serializers
from BigBuyAPI.models.role import Role
from BigBuyAPI.models.department import Department
from BigBuyAPI.models.product import Product
from BigBuyAPI.models.productcategory import ProductCategory
from BigBuyAPI.models.brand import Brand

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
