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
		assert False;

	def post(self, request, *args, **kwargs):
		print request.body
		data_in = json.loads(request.body)
		pitch = data_in['pitch']

		if request.path == '/pitches/post':
			pitch_id = models.pitch_pitches.render(pitch)
			response = {"pitchid" : pitch_id}
			j_resp = json.dumps(response)
			return HttpResponse(content=j_resp, content_type='application/json', status=200)
		else:
			assert False 
