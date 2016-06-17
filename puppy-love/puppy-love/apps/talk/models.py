from django.db import models
from apps.speaker.models import speaker
from apps.conference.models import conference
# Create your models here.
class Talk(models.Model):
	title = models.CharField(max_length=20)
	speaker = models.ForeignKey(speaker)
	conference = models.ForeignKey(conference)