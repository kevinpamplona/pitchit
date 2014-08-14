from django.db import models

# Create your models here.
class Pitch(models.Model):
	pitch = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	date = models.DateTimeField('date pitched')
	kudos = models.IntegerField();

