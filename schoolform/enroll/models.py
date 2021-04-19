from django.db import models
from django.urls import reverse
# Create your models here.
class CollageModel(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    since=models.DateField()

    def get_absolute_url(self):
        return reverse("thanku", kwargs={"pk": self.pk})
    