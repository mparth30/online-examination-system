from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
@admin.register(User)
class UserAdminCustom(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Role Info', {'fields': ('role',)}),)
    list_display = ('username','email','role','is_staff')
    list_filter = ('role',)
