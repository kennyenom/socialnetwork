from django.contrib import admin
from .models import *
# Register your models here.

class PostModelForm(admin.ModelAdmin):
    list_display = ['title','author','created_at']

    # fields = ['search']

    

admin.site.register(PostModel,PostModelForm)
admin.site.register(Comment)
