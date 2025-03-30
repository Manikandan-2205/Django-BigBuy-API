from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from cryptography.fernet import Fernet
from django.conf import settings
from .role import Role

class User(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    username = models.CharField(max_length=50, unique=True)
    displayname = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)
    emailid = models.CharField(max_length=100)
    age = models.IntegerField()
    mobileno = models.CharField(max_length=15)
    password = models.CharField(max_length=500)  
    profilename = models.CharField(max_length=200, null=True, blank=True)
    createdby = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedby = models.IntegerField(null=True, blank=True)
    updatedtime = models.DateTimeField(auto_now=True, null=True, blank=True)
    isdeleted = models.CharField(max_length=1, default='N')
    isactive = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = "TB_BB_USER"

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        fernet = Fernet(settings.SECURITY_KEY.encode())  
        encrypted_password = fernet.encrypt(raw_password.encode()).decode()  
        self.password = encrypted_password

    def get_decrypted_password(self):
        fernet = Fernet(settings.SECURITY_KEY.encode())
        return fernet.decrypt(self.password.encode()).decode()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
