from django import forms
from .models import Survey, Question, Answer, User, Entry



class SurveyForm(forms.ModelForm) :
    class Meta:
        model = Survey
        fields = ('title', 'available_start_dt', 'available_end_dt',)

class QuestionForm(forms.ModelForm) :
    class Meta:
        model = Question
        fields = ('title', 'survey_id', 'limit', 'type')

class AnswerForm(forms.ModelForm) :
    class Meta:
        model = Answer
        fields = ('question_id', 'ans_content')

class UserForm(forms.ModelForm) :
    class Meta:
        model = User
        fields = ('name', 'question_id', 'mobile')

class EntryForm(forms.ModelForm):
    class Meta:
        medel = Entry
        fields = ('user_id', 'answer_id', 'response')
