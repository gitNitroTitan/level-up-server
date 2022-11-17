from django.db import models
from models import Gamer, Organizer


class Event(models.Model):

    game = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
