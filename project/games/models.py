from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Game(models.Model):
    name = models.CharField(max_length=50)
    gamefile = models.FileField(upload_to="Games/%d/",blank=True, null=True)
    video = models.URLField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=50)
    mimage = models.FileField(upload_to="Games/main-images/%d/",blank=True, null=True)
    downloaders = models.ManyToManyField(User, related_name='games', blank=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, blank=True, null=True)
    storage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discription = models.TextField(max_length=300, default="An Amazing Game")
    data_added = models.DateField(auto_created=True, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Game, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.FileField(upload_to="Images/%d/",blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')
    def __str__(self):
        return self.game.name
