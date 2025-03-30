from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=50, unique=True)
    isdeleted = models.CharField(max_length=1, default='N')
    isactive = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = "TB_BB_ROLE"
    
    def __str__(self):
        return self.rolename
