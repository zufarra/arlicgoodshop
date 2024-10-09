from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


import uuid

class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()

