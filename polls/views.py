from django.shortcuts import render
from polls.models import Question
# old way - from django.template import loader, RequestContext
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# old way template = loader.get_template('polls/index.html')
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
	response = "Looking at the results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)