from django.shortcuts import render
from .models import Blog, Comment, Genre
#from rest_framework.response import Response

def index(request):
    
    blog_list = Blog.objects.all
    
    content = {
        'blog_list':blog_list
        }

    return render(request, 'index.html', content)

def blogListView(request, *args, **kwargs):
    qs = Blog.objects.all()
    data = {}
    data['content'] = qs
    return render(request, 'blog/blog_list.html', data)
    

def blogDetailedView(request, blog_id, *args, **kwargs):
    obj = Blog.objects.get(id=blog_id)
    return render(request, 'blog/blog_detail.html', {'obj':obj})

def blogCreateForm(request, *args, **kwargs):
    pass

def blogDeleteForm(request, *args, **kwargs):
    pass

def blogCreateComment(request, *args, **kwargs):
    pass

def blogDeleteComment(request, *args, **kwargs):
    pass
