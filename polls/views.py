from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
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

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{
			'question': question,
			'error_message': 'no_q_found',
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


def results(request, question_id):
	# return HttpResponse("You're looking at results of %s" % question_id
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html', {'question':question})

def vote(request, question_id):
	return HttpResponse("You're looking vote of %s" % question_id)



