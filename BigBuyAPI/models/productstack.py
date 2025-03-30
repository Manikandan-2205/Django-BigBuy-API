# BigBuyAPI/models/productstack.py

from django.db import models
from BigBuyAPI.models.product import Product  # Import the Product model

class ProductStack(models.Model):
    id = models.AutoField(primary_key=True)  
    qty = models.IntegerField(null=False)  
    productname = models.ForeignKey(Product, on_delete=models.CASCADE)  
    createdby = models.IntegerField(null=False)  
    createdtime = models.DateTimeField(auto_now_add=True)  
    updatedby = models.IntegerField(null=True, blank=True)  
    updatedtime = models.DateTimeField(auto_now=True, null=True, blank=True)  
    isdeleted = models.CharField(max_length=1, default='N', null=False)  
    isactive = models.CharField(max_length=1, default='N', null=False)  

    class Meta:
        db_table = "TB_BB_PRODUCT_STACK"  

    def __str__(self):
        return f"Stock ID: {self.id}, Qty: {self.qty}, Product: {self.productname}"