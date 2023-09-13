from typing import Any
from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=120)
    event_location = models.CharField(max_length=70)
    date = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.event_title
    
class Applicant(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)