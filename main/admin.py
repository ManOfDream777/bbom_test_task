from django.contrib import admin
from .models import MyUser, Post


class MyUserAdmin(admin.ModelAdmin):
    model = MyUser


class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Post, PostAdmin)
