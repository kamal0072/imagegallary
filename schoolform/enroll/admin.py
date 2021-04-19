from django.contrib import admin

# Register your models here.
from .models import CollageModel

@admin.register(CollageModel)
class CollageModelAdmin(admin.ModelAdmin):
    list_display=['id','name','address','since']
    
