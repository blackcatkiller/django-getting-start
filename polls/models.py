
from django.db import models
from django.utils import timezone
import datetime

# Create your models here


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

