from django.contrib import admin
from .models import Contact,Post
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Contact)
admin.site.register(Post)
