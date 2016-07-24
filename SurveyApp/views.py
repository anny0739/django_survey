from django.shortcuts import render, get_object_or_404, redirect
import logging
from .forms import SurveyForm, QuestionForm, AnswerForm, UserForm, EntryForm
from .models import Survey, Question, Answer, User, Entry



# Create your views here.

logger = logging.getLogger(__name__)

def survey_list(request) :
    survey_list = Survey.objects.all()
    return render(request, 'SurveyApp/survey_list.html', {'survey_list':survey_list})

def survey_detail(request, id) :
    #survey_detail = get_object_or_404(Survey, id=id)
    survey = Survey.objects.filter(id=id)
    question = Question.objects.filter(survey_id=survey).select_related().values('title', 'limit', 'type')
    logger.error(question)
    return render(request, 'SurveyApp/survey_detail.html', {'survey':survey, 'question':question})

def survey_form(request) :

    if request.method == 'POST' :
        form = SurveyForm()
        survey = form.save(commit=False)
        survey.save()

        form = QuestionForm()
        question = form.save(commit=False)
        survey = Survey.objects.get(id=survey.id)
        question.survey_id = survey
        question.title = request.POST['question_title']
        question.limit = request.POST['limit']
        question.save()

        return redirect('SurveyApp.views.survey_detail', id=survey.id)
    else :
        form = SurveyForm()
        return render(request, 'SurveyApp/survey_form.html', {'form' : form})

#def insert_survey(request) :
    #form = request.POST
    #survey = form.save(commit=False)
    #question = form.save(commit=False)
    #question.survey_id = survey.id
    #survey.save()
    #question.save()


    #titleArr = request.POST['title'];
    #offset = 0
    #for(tit in titleArr) {

    #question = Question.objects.create(survey_id =survey.id,
#        type = request.POST['type'], limit = request.POST['limit'],
#        title = request.POST['question_title']
#    )
#        offset++;
#    }
