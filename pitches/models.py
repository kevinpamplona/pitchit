from django.db import models
from django.utils import timezone

#class PitchManager(models.Manager):
#	@staticmethod
#	def make_pitch(pitch):
#		return Pitch(pitch = pitch)

# Create your models here.
class Pitch(models.Model):
	pitch = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	kudos = models.IntegerField();
	#objects = PitchManager()

class PitchesModel:

	def __init__(self):
		print "PitchesModel initiated"

	def render(self, pitch):
		rendered_pitch = Pitch(pitch = pitch, date=timezone.now, author='chris', kudos=0)
		rendered_pitch.save()
		return rendered_pitch.pk

pitch_pitches = PitchesModel()
