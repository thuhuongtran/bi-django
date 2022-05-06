import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from mysite.polls.models import Question


def save_question():
    print(Question.objects.all())
    from django.utils import timezone
    q = Question(question_text="What's new?", pub_date=timezone.now())
    q.save()
    print(Question.objects.all())


def filter_question():
    print(Question.objects.filter(id=1))
    print(Question.objects.filter(question_text__startswith='What'))
    current_year = timezone.now().year
    print(Question.objects.get(pub_date__year=current_year))
    q = Question.objects.get(pk=1)
    print(q.choice_set.all())


def test_was_published_recently_with_future_question(self):
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    self.assertIs(future_question.was_published_recently(), False)


def test_was_published_recently_with_old_question(self):
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
