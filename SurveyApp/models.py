from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=50)
    available_start_dt = models.DateTimeField(default=timezone.now)
    available_end_dt = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Survey id={0!r}, title={1!r}, available_dt={2!r}>".\
                format(self.id, self.title, self.available_dt)

class SurveyInfo(Survey):
    #survey_id=models.ForeignKey('SuveyApp.Survey')
    #survey_id = models.ForeignKey('SurveyApp.Survey', on_delete=models.CASCADE)
    type = models.CharField(max_length=15, null=False)
    limit = models.IntegerField()

    def __str__(self):
        return self.type

class Question(models.Model):
    surveyInfo_id = models.ForeignKey('SurveyApp.SurveyInfo', on_delete=models.CASCADE)
    contents = models.TextField(null=False)

    def __str__(self):
        return self.contents

class User(models.Model):
    survey_id = models.ForeignKey('SurveyApp.SurveyInfo', on_delete=models.CASCADE, default='0')
    mobile = models.CharField(max_length=13)
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Answer(models.Model):
    user_id = models.ForeignKey('SurveyApp.User')
    question_id = models.ForeignKey('SurveyApp.Question')
    etc = models.TextField()

    def __str__(self):
        return self.name
