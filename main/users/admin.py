from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass