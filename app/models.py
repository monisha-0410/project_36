from django.db import models

# Create your models here.

class School(models.Model):
    s_name=models.CharField(max_length=100)
    s_principal=models.CharField(max_length=100)