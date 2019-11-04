from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        flat_number = models.CharField(max_length=30)
        mobile_number = models.CharField(max_length=30)
        pro_pic=models.ImageField(upload_to='images',blank=True,null=True)
        def __str__(self):
            return self.user.username
