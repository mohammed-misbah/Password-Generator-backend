from django.db import models

# Create your models here.


class GeneratePassword(models.Model):
    password = models.TextField()
