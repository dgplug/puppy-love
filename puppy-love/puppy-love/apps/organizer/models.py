from django.db import models
from apps.conference.models import Conference
from apps.organization.models import Organization
# Create your models here.
class Organizer(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	organization = models.Foreignkey(Organization)

class Selection_Commitee(models.Model):
	organizer = models.Foreignkey(Organizer)
	conference = models.Foreignkey(Conference)