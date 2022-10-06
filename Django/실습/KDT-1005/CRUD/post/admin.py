from django.contrib import admin
from .models import post

# Register your models here.


class postAdmin(admin.ModelAdmin):
    fields = ["title", "content"]


admin.site.register(post, postAdmin)
