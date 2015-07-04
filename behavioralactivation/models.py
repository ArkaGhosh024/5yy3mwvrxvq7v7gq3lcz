from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class UserSchedule(models.Model):
    sleeping = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    pleasure = models.IntegerField(default=0)
    rumination = models.IntegerField(default=0)
    distractionAndAvoidance = models.IntegerField(default=0)
    miscellaneous = models.IntegerField(default=0)
    week = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.user.name
        
    