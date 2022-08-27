from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import datetime

class Genre(models.Model):
    genre = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.genre
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=5000)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, to_field='genre')
    date = datetime.now()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE,to_field='id')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, blank=False)
    def __str__(self):
        return self.text