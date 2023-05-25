from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name="profile", on_delete=models.CASCADE, verbose_name='user')
    bio = models.TextField(max_length = 90, blank=True, null=True)
    image = models.FileField(upload_to="Accounts/users/profiles-images/%d/",blank=True, null=True)
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.user.username
    
