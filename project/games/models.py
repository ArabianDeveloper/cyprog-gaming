from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Game(models.Model):
    name = models.CharField(max_length=50)
    video = models.URLField(max_length=255)
    mimage = models.URLField(max_length=255)
    # downloaders = models.ManyToManyField(User)
    rate = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, blank=True, null=True)
    storage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discription = models.TextField(max_length=300, default="An Amazing Game")
    data_added = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return self.url
