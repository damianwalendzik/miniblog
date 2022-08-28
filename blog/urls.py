from unicodedata import name
from django.urls import path, include
from .views import index, blogDetailedView, blogListView, blogCreateForm
urlpatterns = [
    path('', index, name='index'),
    path('bloglist/', blogListView, name='blog_list'),
    path('bloglist/<uuid:blog_id>/', blogDetailedView, name='blog_detail'),
    path('create-blog/', blogCreateForm, name='create_blog'),
]