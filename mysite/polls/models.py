import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField(max_length = 200)
  date_published = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text
  def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  choice_text = models.CharField(max_length = 200)
  question = models.ForeignKey(Question, on_delete = models.CASCADE)
  votes = models.IntegerField(default = 0)
  def __str__(self):
    return self.choice_text



