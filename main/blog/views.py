from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from blog.models import BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog-details.html'
    context_object_name = 'blog_detail'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        qs = BlogPost.objects.all()
        return qs


