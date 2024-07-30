from django.db import models

class Score(models.Model):
    Red = models.IntegerField(default=0)
    Orange = models.IntegerField(default=0)
    Yellow = models.IntegerField(default=0)
    Green = models.IntegerField(default=0)
    Blue = models.IntegerField(default=0)
    
    last_updated = models.DateTimeField(default=0)
