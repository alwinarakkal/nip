from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.core.exceptions import PermissionDenied

# from phone_field import PhoneField

class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        flat_number = models.CharField(max_length=30)
        mobile_number = models.CharField(max_length=20)
        # mobile_number = PhoneField(blank=False, help_text='Enter valid number')
        pro_pic=models.ImageField(upload_to='images',blank=True,null=True)
        def __str__(self):
            return self.user.username

@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    if instance.is_superuser:
        raise PermissionDenied