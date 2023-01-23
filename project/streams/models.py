from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Stream(models.Model):
    STATUS = [
        {'Live' : 'Live'},
        {'Finished' : 'Finished'}
    ]


    title = models.CharField(max_length=50)
    # streamer = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.URLField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    # viewers = models.ManyToManyField(User)
    # status = models.Choices(STATUS)

    def __str__(self):
        return self.title