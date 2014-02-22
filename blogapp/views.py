from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("The future has been happening for some time now.")

def current(request):
	time = "time to get started"
	return render_to_response('time.html', {'current_time':time})
