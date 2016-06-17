from django.db import models

# Create your models here.

class Conference(models.Model):
	name = models.CharField(max_length=40)
	start_date = models.DAteTimeField()
	end_date = models.DAteTimeField()
	location = models.CharField(max_length=20)