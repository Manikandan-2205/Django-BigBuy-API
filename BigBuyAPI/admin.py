from django.contrib import admin

from .models.brand import Brand
from .models.department import Department
from .models.order import Order
from .models.ordertransaction import OrderTransaction
from .models.product import Product
from .models.productcategory import ProductCategory
from .models.productstack import ProductStack
from .models.role import Role
from .models.user import User
from .models.useraddress import UserAddress
from .models.jwttoken import Jwttoken

admin.site.register(Brand)
admin.site.register(Department)
admin.site.register(Order)
admin.site.register(OrderTransaction)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductStack)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(Jwttoken)