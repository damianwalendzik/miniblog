from django.contrib import admin
from .models import Blog, Comment, Genre
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Genre)

# Register your models here.
class BlogInstanceInline(admin.TabularInline):
    model = Blog

class CommentInstanceInline(admin.TabularInline):
    model = Comment

class GenreInstanceInline(admin.TabularInline):
    model = Genre

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogInstanceInline]
