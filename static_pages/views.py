from django.shortcuts import render

# Create your views here.
def static_asset(request):
    f = open(curdir + sep + request.path)
    if request.path.endswith(".html"):
            _content_type = 'text/html'
    elif request.path.endswith(".css"):
            _content_type = 'text/css'
    elif request.path.endswith(".js"):
            _content_type = 'text/javascript'
    else:
            assert False
    response = HttpResponse(content=f.read(), content_type=_content_type, status=200)
    f.close()
    return response

def static_page(request):
    context = {}
    if request.method == 'GET':
        if request.user.is_authenticated():
            context['logged_in'] = True
        else:
            context['logged_in'] = False
    else:
        # should not reach here
        context['message'] = "Yo, you wrong!"

    context['username'] = request.user.username 
    return render(request, 'static_pages/index.html', context)