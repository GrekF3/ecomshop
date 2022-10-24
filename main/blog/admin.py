from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class Blog_Admin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
