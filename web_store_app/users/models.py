from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class WebsiteUser(AbstractUser):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    phone_number = models.IntegerField(null=True)
    address = models.TextField(null=True)
    wallet = models.IntegerField(null=True, default=0)
