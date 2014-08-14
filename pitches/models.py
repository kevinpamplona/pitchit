from django.db import models

# Create your models here.
class Pitch(models.Model):
	pitch = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	date = models.DateTimeField('date pitched')

	def __unicode__(self):
		return self.pitch

class Tag(models.Model):
	tag = models.CharField(max_length=200)

	def __unicode__(self):
		return self.tag

class PitchTag(models.Model):
	pitch_id = models.ForeignKey(Pitch)
	tag_id = models.ForeignKey(Tag)