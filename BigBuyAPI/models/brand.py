from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brandname = models.CharField(max_length=50)
    createdby = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedby = models.IntegerField(null=True, blank=True)
    updatedtime = models.DateTimeField(auto_now=True, null=True, blank=True)
    isdeleted = models.CharField(max_length=1, default='N')
    isactive = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = "TB_BB_PRODUCT_BRAND"

    def __str__(self):
        return self.brandname
