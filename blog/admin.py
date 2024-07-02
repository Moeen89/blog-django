from django.contrib import admin

from .models import Post,Writer

admin.site.register(Post)
admin.site.register(Writer)