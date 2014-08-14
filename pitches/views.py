from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("making tubemogul a better place to work, one pitch at a time")

def detail(request, pitch_id):
    return HttpResponse("You're looking at pitch %s." % pitch_id)