from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
    return render_to_response('pages/index.html', context_instance=RequestContext(request))


def style(request):
	return render_to_response('assets/stylesheets/styledafasd.css', context_instance=RequestContext(request))