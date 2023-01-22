from django.db import models

# Create your models here.

class Images(models.Model):
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.url



class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Game(models.Model):
    name = models.CharField(max_length=50)
    video = models.URLField(max_length=255)
    images = models.ManyToManyField(Images)
    # downloaders
    rate = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, blank=True, null=True)
    storage = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    discription = models.TextField(max_length=300, default="An Amazing Game")


    def __str__(self):
        return self.name