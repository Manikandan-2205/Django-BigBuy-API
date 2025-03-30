from django.db import models
from .order import Order

class OrderTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    remark = models.CharField(max_length=1000, null=True, blank=True)
    createdby = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedby = models.IntegerField(null=True, blank=True)
    updatedtime = models.DateTimeField(auto_now=True, null=True, blank=True)
    isdeleted = models.CharField(max_length=1, default='N')
    iscanceled = models.CharField(max_length=1, default='N')
    isreturn = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = "TB_BB_ORDERR_TRANS"

    def __str__(self):
        return f"OrderTransaction ID: {self.id}, Order ID: {self.orderid.id}"
