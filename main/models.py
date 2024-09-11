from django.db import models

# Create your models here.
from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

