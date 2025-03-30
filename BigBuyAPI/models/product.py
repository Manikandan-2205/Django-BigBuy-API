# BigBuyAPI/models/product.py

from django.db import models
from .productcategory import ProductCategory
from .brand import Brand

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=50)
    productcategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    createdby = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedby = models.IntegerField(null=True, blank=True)
    updatedtime = models.DateTimeField(auto_now=True, null=True, blank=True)
    isdeleted = models.CharField(max_length=1, default='N')
    isactive = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = "TB_BB_PRODUCT"

    def __str__(self):
        return self.productname


class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.ForeignKey(Product, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    imageurl = models.CharField(max_length=300)
    yearofmanufacturing = models.IntegerField()
    rate = models.DecimalField(max_digits=7, decimal_places=3)
    createdby = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedby = models.IntegerField(null=True, blank=True)
    updatedtime = models.DateTimeField(auto_now=True, null=True, blank=True)
    isdeleted = models.CharField(max_length=1, default='N')
    isactive = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = "TB_BB_PRODUCT_DETAILS"

    def __str__(self):
        return f"{self.productname} - {self.model} - {self.color}"