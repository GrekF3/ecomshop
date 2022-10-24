from django.urls import path

from blog.views import BlogPostDetailView, BlogListView
from shop import views



urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>', BlogPostDetailView.as_view(), name='blog_detail'),
]

