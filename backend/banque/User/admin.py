from django.contrib import admin
from .models import User
class AdminUser(admin.ModelAdmin):
    list_display = [
        "email", "username","first_name","last_name","password"
    ]
admin.site.register(User, AdminUser)