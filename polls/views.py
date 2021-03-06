from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
    #
    # Return the last five published questions (not including those set to be
    # published in the future).
    #
	def get_queryset(self):
		# return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	template_name = 'polls/detail.html'
	model = Question

class ResultsView(generic.DetailView):
	template_name = 'polls/result.html'
	model = Question

def vote(request, question_id):
	return HttpResponse("You're looking vote of %s" % question_id)

