from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)

def detail(request, question_id):
	return HttpResponse("You're looking at %s" % question_id)

def results(request, question_id):
	return HttpResponse("You're looking at results of %s" % question_id)

def vote(request, question_id):
	return HttpResponse("You're looking vote of %s" % question_id)



