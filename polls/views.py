from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	# output = ', '.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)
	
	# return HttpResponse(template.render(context,request))
	return render(request, 'polls/index.html', context)
	

def detail(request, question_id):
	# return HttpResponse("You're looking at %s" % question_id)
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('Not_found')
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	return HttpResponse("You're looking at results of %s" % question_id)

def vote(request, question_id):
	return HttpResponse("You're looking vote of %s" % question_id)



