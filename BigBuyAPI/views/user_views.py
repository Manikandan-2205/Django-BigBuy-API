from django.conf import settings
from cryptography.fernet import Fernet
from django.db import models
from BigBuyAPI.models.user import User
from BigBuyAPI.models.useraddress import UserAddress
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from BigBuyAPI.serializers.user_serializers import UserSerializer, UserAddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def encrypt_password(self, raw_password):
        """Encrypts the password using Fernet encryption."""
        fernet = Fernet(settings.SECURITY_KEY.encode())
        return fernet.encrypt(raw_password.encode()).decode()

    @swagger_auto_schema(
        operation_description="Retrieve all users",
        responses={200: UserSerializer(many=True)},
    )
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve a user by ID", responses={200: UserSerializer()}
    )
    def retrieve(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=UserSerializer,
        responses={201: UserSerializer()},
    )
    def create(self, request):
        """Encrypts password before creating a user."""
        data = request.data.copy()  # Copy request data
        if "password" in data:
            data["password"] = self.encrypt_password(
                data["password"]
            )  # Encrypt password

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a user by ID",
        request_body=UserSerializer,
        responses={200: UserSerializer()},
    )
    def update(self, request, pk=None, *args, **kwargs):
        user = self.get_object()
        partial = kwargs.get("partial", False)
        data = request.data.copy()

        if "password" in data and data["password"]:
            data["password"] = self.encrypt_password(data["password"])

        serializer = self.get_serializer(user, data=data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAddressViewSet(viewsets.ModelViewSet):
    """
    User Address
    """

    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    @swagger_auto_schema(
        operation_description="Retrieve all user addresses",
        responses={200: UserAddressSerializer(many=True)},
    )
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve a user address by ID",
        responses={200: UserAddressSerializer()},
    )
    def retrieve(self, request, pk=None):
        address = self.get_object()
        serializer = self.get_serializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new user address",
        request_body=UserAddressSerializer,
        responses={201: UserAddressSerializer()},
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a user address by ID",
        request_body=UserAddressSerializer,
        responses={200: UserAddressSerializer()},
    )
    def update(self, request, pk=None):
        address = self.get_object()
        serializer = self.get_serializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
