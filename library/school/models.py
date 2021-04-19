from django.db import models

# Create your models here.
class BookMode(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=1000)
    publish_date=models.DateTimeField()