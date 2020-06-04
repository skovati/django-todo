from django.db import models
from django.utils import timezone

class Item(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.content
