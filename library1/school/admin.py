from django.contrib import admin
from .models import BookMode
# Register your models here.

@admin.register(BookMode)
class BookModeAdmin(admin.ModelAdmin):
    list_display=['id','name','desc','publish_date']
    
