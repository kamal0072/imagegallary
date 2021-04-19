from django.db import models

# Create your models here.
class CollageModel(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    start_year=models.DateField()