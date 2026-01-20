from django.db import models
from ConferenceApp.models import Conference


# Create your models here.
class Session(models.Model):
    title = models.CharField(max_length=200)
    session_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.IntegerField()
    topic = models.CharField(max_length=200)

    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name="sessions"
    )
