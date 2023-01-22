from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class stream(models.Model):
    title = models.CharField(max_length=50)
    # streamer = models.ForeignKey()
    image = models.URLField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    # viewers = models.ManyToManyField()


    def __str__(self):
        return self.title