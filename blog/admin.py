from django.contrib import admin
from .models import Category,Post
# Register your models here.

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','status','slug','author']