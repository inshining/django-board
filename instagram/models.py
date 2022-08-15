from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.CharField(max_length= 200, verbose_name="메세지")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)