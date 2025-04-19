from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    activity_level = models.CharField(max_length=50)
    dietary_preferences = models.CharField(max_length=255)
    goal = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username