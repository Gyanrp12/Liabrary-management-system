from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(User)
class User_admin(admin.ModelAdmin):
    list_display = ['id', 'email']


@admin.register(IssuedBook)
class User_admin(admin.ModelAdmin):
    list_display = ['id', 'book', 'student_id']


@admin.register(Book)
class User_admin(admin.ModelAdmin):
    list_display = ['id', 'name']
