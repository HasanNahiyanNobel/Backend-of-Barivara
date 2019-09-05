from django.http import HttpResponse

# Create your views here.


def index(request):
	html = '<h1>Hey Jude!</h1>'
	return HttpResponse(html)