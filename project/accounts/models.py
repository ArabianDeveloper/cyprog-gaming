from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length = 90, blank=True, null=True)
    image = models.URLField(max_length = 255, blank=True, null=True)
