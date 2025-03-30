from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BigBuyAPI.views.user_views import UserViewSet, UserAddressViewSet
from BigBuyAPI.views.order_views import OrderViewSet,OrderTransactionViewSet

from BigBuyAPI.views.product_views import (
    ProductViewSet,
    ProductCategoryViewSet,
    ProductDetailsViewSet,
    BrandViewSet,
    ProductStackViewSet,
)

from BigBuyAPI.views.manage_master_view import (
    DepartmentMaster,
    RoleMasters,
)

# Create a router and register your viewsets
router = DefaultRouter()

# User Management
router.register(r"users", UserViewSet, basename="user")
router.register(r"user-address", UserAddressViewSet, basename="user-address")

# Order Management
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"order-tran", OrderTransactionViewSet, basename="order-tran")

# Product Management
router.register(r"brand", BrandViewSet, basename="brand")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"prod-details", ProductDetailsViewSet, basename="prod-details")
router.register(
    r"prod-category", ProductCategoryViewSet, basename="prod-category"
)
router.register(r"prod-stack", ProductStackViewSet, basename="prod-stack")

# master management
router.register(r"role", RoleMasters, basename="role-masters")
router.register(r"dep", DepartmentMaster, basename="dep")

urlpatterns = [
    path("", include(router.urls)),
]
