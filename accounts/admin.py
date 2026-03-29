from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from drivers.models import DriverProfile

class CustomUserAdmin(UserAdmin):
    fieldsets = list(UserAdmin.fieldsets) + [
        ('Carlift Profile Info', {'fields':('role', 'phone_number', 'profile_pic')}),
    ]

    list_display = ['username', 'role', 'email','is_staff']



admin.site.register(User,CustomUserAdmin)
admin.site.register(DriverProfile)
