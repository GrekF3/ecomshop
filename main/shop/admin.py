from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    pass

class BrandAdmin(admin.ModelAdmin):
    pass

class GalleryAdmin(admin.ModelAdmin):
    pass
@admin.register(Ad)
class AdsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand,BrandAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Gallery,GalleryAdmin)