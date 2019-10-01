from django.contrib import admin
from .models import User

class UserAdmin(User):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


# admin.site.register(User, UserAdmin)