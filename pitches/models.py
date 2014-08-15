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
<<<<<<< HEAD
	date = models.DateTimeField(auto_now_add=True)
	kudos = models.IntegerField();
	#objects = PitchManager()

	def __unicode__(self):
		return self.pitch

class Tag(models.Model):
	tag = models.CharField(max_length=200)

	def __unicode__(self):
		return self.tag

class PitchTag(models.Model):
	pitch_id = models.ForeignKey(Pitch)
	tag_id = models.ForeignKey(Tag)

	def __unicode__(self):
		pitch_id_ref = self(pitch_id)
		tag_id_ref = sel

class PitchKudo(models.Model):
	kudo = models.IntegerField();
=======
	date = models.DateTimeField('date pitched')
	kudos = models.IntegerField();
>>>>>>> cf61da600b2561548f40dc5fc6de0d181a935813

class PitchesModel:

	def __init__(self):
		print "PitchesModel initiated"

	def render(self, pitch):
		rendered_pitch = Pitch(pitch = pitch, date=timezone.now, author='chris', kudos=0)
		rendered_pitch.save()
		return rendered_pitch.pk

pitch_pitches = PitchesModel()
