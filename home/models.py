from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    publishTime = models.DateTimeField(default=timezone.now)
    thumbnail_url = models.CharField(max_length=350)
    url = models.CharField(max_length=200)
    channelTitle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title + ' by ' + self.channelTitle