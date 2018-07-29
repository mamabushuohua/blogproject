from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'anthor']

    admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
