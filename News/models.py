from django.db import models


# Create your models here.

class NewsContent(models.Model):
    title = models.CharField(max_length=128)
    new_content = models.CharField(max_length=9999)
