from django.db import models
from models import Gamer, Event



class EventGamer(models.Model):

    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
