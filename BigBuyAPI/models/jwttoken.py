from django.db import models
from .user import User

class Jwttoken(models.Model):
    id = models.AutoField(primary_key=True)
    jwttoken = models.CharField(max_length=300)
    tokenexpiredtime = models.DateTimeField()
    tokenstatus = models.CharField(max_length=1, db_default="N")
    createdby = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TB_BB_JWTTOKEN"

    def __str__(self):
        return self.jwttoken

class UserLog(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    tokenid = models.ForeignKey(Jwttoken, on_delete=models.CASCADE)  # Corrected foreign key
    logintime = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    logouttime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "TB_BB_USERLOG"

    def __str__(self):
        return str(self.id)