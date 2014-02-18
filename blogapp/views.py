from django.http import HttpResponse

def hello(request):
	return HttpResponse("The future has been happening for some time now.")