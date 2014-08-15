from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.core.exceptions import ObjectDoesNotExist
from os import curdir, sep
#import pitches.models import Pitch
import json
import models

# Create your views here.
def index(request):
    return HttpResponse("making tubemogul a better place to work, one pitch at a time")

def detail(request, pitch_id):
    return HttpResponse("You're looking at pitch %s." % pitch_id)

class RenderView(View):
	def get(self, request, *args, **kwargs):
		#data_in = json.loads(request.body)
		if request.path == '/pitches/get':
			pitches_list = models.pitch_pitches.get_pitches()
			print pitches_list
		
		pitches_data = []
		
		for pitch in pitches_list:
			# pitch = ['pitch', 'author', 'date', 'kudos']
			pitch_dict = {}
			pitch_dict['pitch'] = pitch[0]
			pitch_dict['author'] = pitch[1]
			pitch_dict['date'] = str(pitch[2])
			pitch_dict['kudos'] = pitch[3]

			pitches_data.append(pitch_dict)

		pitches_data_out = {}
		pitches_data_out['pitches'] = pitches_data


		j_resp = json.dumps(pitches_data_out)

		return HttpResponse(content=j_resp, content_type='application/json', status=200)

	def post(self, request, *args, **kwargs):
		print request.body
		data_in = json.loads(request.body)

		if request.path == '/pitches/post':
			pitch = data_in['pitch']
			pitch_id = models.pitch_pitches.render(pitch)
			response = {"pitchid" : pitch_id}
			j_resp = json.dumps(response)
			return HttpResponse(content=j_resp, content_type='application/json', status=200)
		elif request.path == '/pitches/kudos/post':
			pitch_id = data_in['pitch_id']
			models.pitch_pitches.increase(pitch_id)
			return HttpResponse(status=200)
		else:
			assert False 
