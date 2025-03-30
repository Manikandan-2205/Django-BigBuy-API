from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from BigBuyAPI.models.department import Department
from BigBuyAPI.models.role import Role

from BigBuyAPI.serializers.manage_master_serializers import (
    DepartmentSerializer,
    RoleSerializer,
)


class DepartmentMaster(viewsets.ModelViewSet):
    """
    Department Master Details
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @swagger_auto_schema(
        operation_description="Department Master Details",
        request_body=DepartmentSerializer,
        responses={201: DepartmentSerializer()},
    )
    def Department(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class RoleMasters(viewsets.ModelViewSet):
    """
    Role Master Details
    """

    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    @swagger_auto_schema(
        operation_description="Product Category Masters Details",
        request_body=RoleSerializer,
        responses={201: RoleSerializer()},
    )
    def Brand(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
