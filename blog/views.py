from django.shortcuts import render
from .models import Blog, Comment, Genre

def index(request):
    
    blog_list = Blog.objects.all
    
    content = {
        'blog_list':blog_list
        }

    return render(request, 'index.html', content)