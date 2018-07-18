# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns false for questions who pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(futureQuestion.was_published_recently(), False)
