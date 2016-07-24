from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=50)
    available_start_dt = models.DateTimeField(default=timezone.now)
    available_end_dt = models.DateTimeField(default=timezone.now)

    #class Meta:
    #    abstract = True
    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Survey id={0!r}, title={1!r}, available_start_dt={2!r}, available_end_dt={3!r}>".\
                format(self.id, self.title, self.available_start_dt, self.available_end_dt)

class Question(models.Model):
    #survey_id=models.ForeignKey('SuveyApp.Survey')
    survey_id = models.ForeignKey('SurveyApp.Survey', on_delete=models.CASCADE, default='0')
    type = models.CharField(max_length=15, default='select')
    limit = models.IntegerField(default=0)
    title = models.TextField()

    def __str__(self):
        return self.type

class Answer(models.Model):
    question_id = models.ForeignKey('SurveyApp.Question', on_delete=models.CASCADE)
    content = models.TextField(null=False)

    def __str__(self):
        return self.content

class User(models.Model):
    question_id = models.ForeignKey('SurveyApp.Question', on_delete=models.CASCADE, default='0')
    mobile = models.CharField(max_length=13)
    name = models.CharField(max_length=20, null=False, default='0')

    def __str__(self):
        return self.name

class Entry(models.Model):
    user_id = models.ForeignKey('SurveyApp.User')
    answer_id = models.ForeignKey('SurveyApp.Answer')
    response = models.TextField()

    def __str__(self):
        return self.response
