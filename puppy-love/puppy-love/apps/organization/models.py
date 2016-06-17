from django.db import models
from apps.conference.models import Conference
# Create your models here.
class Organization(models.Model):
	name = models.CharField()

class Sponsor(models.Model):
	conference = models.Foreignkey(Conference)
	organization = models.Foreignkey(Organization)