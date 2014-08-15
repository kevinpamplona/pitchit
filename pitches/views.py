from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.core.exceptions import ObjectDoesNotExist
from os import curdir, sep
from django.core.mail import send_mail
#import pitches.models import Pitch
import json
import models

# Create your views here.
def email(request):
	top_kudos = models.pitch_pitches.top_pitches()
	pitch1 = top_kudos[0]
	pitch2 = top_kudos[1]
	pitch3 = top_kudos[2]

	str1 = "[[" + pitch1.title + "]]: " + pitch1.description + " -- currently with " + str(pitch1.kudos) + " kudos!"
	str2 = "[[" + pitch2.title + "]]: " + pitch2.description + " -- currently with " + str(pitch2.kudos) + " kudos!"
	str3 = "[[" + pitch3.title + "]]: " + pitch3.description + " -- currently with " + str(pitch3.kudos) + " kudos!"

	str_out = str1 + "\n" + str2 + "\n" + str3

	send_mail('PITCHR TOP', 'TOP 3 pitches!:::\n' + str_out, 'kevinpamplona@gmail.com', ['chris.schechter@tubemogul.com', 'kevin.pamplona@tubemogul.com, vicki.hsu@tubemogul.com, andrew.wang.tubemogul.com, kevin.lee@tubemogul.com'])


	return HttpResponse("making tubemogul a better place to work, one pitch at a time")

def index(request):
    return HttpResponse("making tubemogul a better place to work, one pitch at a time")

def detail(request, pitch_id):
    return HttpResponse("You're looking at pitch %s." % pitch_id)

class RenderView(View):
	def get(self, request, *args, **kwargs):
		#data_in = json.loads(request.body)
		if request.path == '/pitches/get':
			pitches_list = models.pitch_pitches.get_pitches()
		pitches_data = []
		
		for pitch in pitches_list:
			# pitch = ['pitch', 'author', 'date', 'kudos']
			pitch_dict = {}
			pitch_dict['id'] = pitch[0]
			pitch_dict['title'] = pitch[1]
			pitch_dict['description'] = pitch[2]
			pitch_dict['author'] = str(pitch[3])
			#pitch_dict['date'] = pitch[4]
			pitch_dict['kudos'] = pitch[4]

			pitches_data.append(pitch_dict)

		pitches_data_out = {}
		pitches_data_out['pitches'] = pitches_data


		j_resp = json.dumps(pitches_data_out)
		print j_resp
		return HttpResponse(content=j_resp, content_type='application/json', status=200)

	def post(self, request, *args, **kwargs):
		#print request.body
		data_in = json.loads(request.body)
		# data_in = json.loads(request.body.replace("\'", '"'))

		if request.path == '/pitches/post':
			title = data_in['title']
			description = data_in['description']
			pitch_id = models.pitch_pitches.render(title, description)
			response = {"pitchid" : pitch_id}
			j_resp = json.dumps(response)
			return HttpResponse(content=j_resp, content_type='application/json', status=200)
		elif request.path == '/pitches/kudos/post':
			pitch_id = data_in['pitch_id']
			kudo_count = models.pitch_pitches.increase(pitch_id)
			pitch_kudos = {}
			pitch_kudos['kudo'] = kudo_count;
			j_resp = json.dumps(pitch_kudos)
			return HttpResponse(content=j_resp, content_type='application/json', status=200)
		elif request.path == '/pitches/kudos/take':
			pitch_id = data_in['pitch_id']
			kudo_count = models.pitch_pitches.decrease(pitch_id)
			pitch_kudos = {}
			pitch_kudos['kudo'] = kudo_count;
			j_resp = json.dumps(pitch_kudos)
			return HttpResponse(content=j_resp, content_type='application/json', status=200)
		else:
			assert False 
