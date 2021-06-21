from django.db import models


# Create your models here.
from django.urls import reverse




class News(models.Model):
    img = models.ImageField(upload_to='gallery')
    topic = models.CharField(max_length=250)
    desc = models.TextField()
    name = models.CharField(max_length=250)
    desc1 = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)
