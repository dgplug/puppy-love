from django.db import models
from apps.organization.models import Organization
# Create your models here.
class Speaker(models.Model):
	first_name = models.CharField()
	last_name = models.CharField()
	organization = models.Foreignkey(Organization)