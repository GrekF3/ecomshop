from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand_name",)}

class GalleryAdmin(admin.TabularInline):
    fk_name = 'product'
    model = Gallery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [GalleryAdmin,]

@admin.register(Ad)
class AdsAdmin(admin.ModelAdmin):
    pass

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass