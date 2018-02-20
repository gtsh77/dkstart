import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Question

def create_question(question_text, days):
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
    #
    # If no questions exist, an appropriate message is displayed.
    #		
	def test_no_question(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response,"No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'],[])
    #
    # Questions with a pub_date in the past are displayed on the
    # index page.
    #
	def test_past_question(self):
		create_question(question_text="past_q",days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
			['<Question: past_q>'])

	def test_future_question(self):
		create_question(question_text="future_q",days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response,"No polls are available.")

	def test_future_question_and_past_question(self):
		create_question(question_text="past_q",days=-30)
		create_question(question_text="future_q",days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
			['<Question: past_q>'])

	def two_past_questions(self):
		create_question(question_text="past_q_1",days=-30)
		create_question(question_text="past_q_2",days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
			['<Question: past_q_2>','<Question: past_q_1>'])