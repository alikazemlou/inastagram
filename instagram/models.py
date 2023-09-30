from django.db import models

# Create your models here.
class post(models.Model):
    create_at = models.DateTimeField()
    title = models.CharField(max_length=400)
    body = models.TextField()