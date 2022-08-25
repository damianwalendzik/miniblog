from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import datetime

class Genre(models.Model):
    genre = models.CharField(max_length=20)

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=5000)
    genre = models.ForeignKey(Genre)
    date = datetime.now()

class comments(models.Model):
    blog = models.ForeignKey(Blog, to_field=id)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
