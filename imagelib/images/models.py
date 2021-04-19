from django.db import models
# from geography.models import ZipCode

class MyImage(models.Model):
    first_name = models.CharField("person's first name", max_length=30)
    # id = models.BigAutoField(primary_key=True)
    photo=models.ImageField(upload_to='kkimages')
    date=models.DateTimeField(auto_now=True)
