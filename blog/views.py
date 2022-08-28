from django.shortcuts import render
from .models import Blog, Comment, Genre
from .forms import CreateNewBlog
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
    comments = Comment.objects.filter(blog=blog_id)
    data = {
        'obj':obj,
        'comments':comments
    }
    return render(request, 'blog/blog_detail.html', data)

def blogCreateForm(request, *args, **kwargs):
    if request.POST:
        form = CreateNewBlog(request.POST)
        print(form)
        if form.is_valid():
            new_title = form.cleaned_data["title"]
            new_text = form.cleaned_data["text"]
            new_author= form.cleaned_data["author"]
            new_genre=form.cleaned_data["genre"]
            new_blog = Blog(title=new_title, author=new_author, text=new_text, genre=new_genre)
            #new_blog.author = request.author
            new_blog.save()
    else:
        form = CreateNewBlog()
    return render(request, 'blog/create_blog.html',{'form':form})

def blogDeleteForm(request, *args, **kwargs):
    pass

def blogCreateComment(request, *args, **kwargs):
    pass

def blogDeleteComment(request, *args, **kwargs):
    pass
