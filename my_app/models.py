from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=200)
    calories = models.FloatField()

    def __str__(self):
        return self.title
    
