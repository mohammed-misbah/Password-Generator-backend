from django.db import models

# Create your models here.


class GeneratePassword(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.TextField()

    def __str__(self):  
        return f"{self.username}'s password"
