from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['email', 'username',]
    list_filter = ['email', 'username',]
    search_fields = ['email', 'username',]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        (
        'Permissions', {'fields': ('is_staff', 'is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

admin.site.register(models.Account, UserAdmin)

# admin.site.register(models.Account)