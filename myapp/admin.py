from django.contrib import admin
from myapp.models import Post, AboutMe

admin.site.register(Post, AboutMe)
# Register your models here.
