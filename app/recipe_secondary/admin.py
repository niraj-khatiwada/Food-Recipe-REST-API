from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username']
    list_filter = ['email', 'username']
    search_fields = ['email', 'username']

admin.site.register(UserAdmin, models.Account)
# admin.site.register(models.Account)