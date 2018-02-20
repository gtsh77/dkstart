# import datetime

# from django.utils import timezone, reverse
# from django.test import TestCase

# # Create your tests here.
# from .models import Question

# class QuestionModelTests(TestCase):
# 	#
# 	# was_published_recently() returns False for questions whose pub_date
# 	# is in the future.
# 	# 	
# 	def test_was_published_recently(self):
# 		time = timezone.now() + datetime.timedelta(days=30)
# 		future_question = Question(pub_date=time)
# 		self.assertIs(future_question.was_published_recently(),False)
#     #
#     # was_published_recently() returns False for questions whose pub_date
#     # is older than 1 day.
#     #
# 	def test_was_published_recently_with_old_question(self):
# 		time = timezone.now() + datetime.timedelta(days=1,seconds=1)
# 		old_question = Question(pub_date=time)
# 		self.assertIs(old_question.was_published_recently(),False)
#     #
#     # was_published_recently() returns True for questions whose pub_date
#     # is within the last day.
#     #
# 	def test_was_published_recentlry_with_recent_question(self):
# 		time = timezone.now() + datetime.timedelta(hours=23,minutes=59,seconds=59)
# 		recent_question = Question(pub_date=time)
# 		self.assertIs(recent_question.was_published_recently(),True)