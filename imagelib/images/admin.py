from django.contrib import admin
from .models import MyImage

@admin.register(MyImage)
class MyImageAdmin(admin.ModelAdmin):
    list_display=['id','first_name','photo','date']
    
