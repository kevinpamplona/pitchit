from django.db import models
from django.utils import timezone

#class PitchManager(models.Manager):
#	@staticmethod
#	def make_pitch(pitch):
#		return Pitch(pitch = pitch)

# Create your models here.
class Pitch(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	kudos = models.IntegerField();
	#objects = PitchManager()

class PitchesModel:

	def __init__(self):
		print "PitchesModel initiated"

	def render(self, title, description):
		rendered_pitch = Pitch(title=title, description=description, date=timezone.now, author='unknown', kudos=0)
		rendered_pitch.save()
		return rendered_pitch.pk

	def increase(self, pitch_id):
		try:
			pitch = Pitch.objects.get(pk=pitch_id)
		except DoesNotExist:
			return null
		count = pitch.kudos
		pitch.kudos += 1
		pitch.save()
		return pitch.kudos

	def decrease(self, pitch_id):
		try:
			pitch = Pitch.objects.get(pk=pitch_id)
		except DoesNotExist:
			return null
		count = pitch.kudos
		pitch.kudos -= 1
		pitch.save()
		return pitch.kudos

	def get_pitches(self):
		pitches = Pitch.objects.values_list('id','title', 'description', 'author', 'kudos')
		return pitches

	def top_pitches(self):
		top = Pitch.objects.order_by('-kudos')
		return top


pitch_pitches = PitchesModel()
