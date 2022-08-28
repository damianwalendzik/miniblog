from urllib import request
from django import forms
from .models import Blog
class CreateNewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'text', 'genre']