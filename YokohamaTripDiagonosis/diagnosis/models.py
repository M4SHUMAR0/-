from django.db import models
from django.utils import timezone

# Create your models here.
class evaluation(models.Model):
    created_time=models.DateTimeField(default=timezone.now)
    evaluation=models.IntegerField()