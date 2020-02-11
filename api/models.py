from django.db import models

# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=60)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + ": " + self.text