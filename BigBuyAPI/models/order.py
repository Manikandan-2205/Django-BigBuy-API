from django.db import models
from .product import Product

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderid = models.CharField(max_length=10, unique=True)
    orderqty = models.IntegerField()
    createdby = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedby = models.IntegerField(null=True, blank=True)
    updatedtime = models.DateTimeField(auto_now=True, null=True, blank=True)
    isdeleted = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = "TB_BB_ORDERR"

    def __str__(self):
        return self.orderid
