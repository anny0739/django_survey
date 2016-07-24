from django.shortcuts import render, get_object_or_404, redirect
import logging
from .forms import SurveyForm, QuestionForm, AnswerForm, UserForm, EntryForm
from .models import Survey, Question, Answer, User, Entry



logger = logging.getLogger(__name__)

def survey_list(request) :
    #설문 목록

    survey_list = Survey.objects.all()
    return render(request, 'SurveyApp/survey_list.html', {'survey_list':survey_list})

def survey_detail(request, id) :
    #survey_detail = get_object_or_404(Survey, id=id)
    #설문 항목

    survey = Survey.objects.filter(id=id)
    question = Question.objects.filter(survey_id=survey).select_related().values('title', 'limit', 'type', 'id')
    q_id = question[0].get('id')
    answer = Answer.objects.filter(question_id=q_id).values('question_id', 'content')

    return render(request, 'SurveyApp/survey_detail.html', {'survey':survey, 'question':question, 'answer':answer})

def survey_form(request) :
    # 설문 생성

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
        question.type = request.POST['type']
        question.save()

        # 임시로 처리 (한 question에 대해서만 입력)
        answer_contents = request.POST.getlist('content')

        answer = AnswerForm()
        answer = form.save(commit=False)
        answer.question_id = question

        for ans in answer_contents :
            answer.content = ans
            Answer.objects.create(question_id=question, content=ans)

        return redirect('SurveyApp.views.survey_detail', id=survey.id)
    else :
        form = SurveyForm()
        return render(request, 'SurveyApp/survey_form.html', {'form' : form})

def survey_register(request) :
    # 설문 응답

    if request.method == 'POST' :
        form = UserForm()
        user = form.save()
        user.save()
        user = Suer.objects.get(id=user.id)

        form = EntryForm()
        entry = form.save(commit=False)
        entry.id = user
        entry.save()
        return redirect('SurveyApp.views.entry_detail', id=user.survey_id)
    else :
        form = UserForm()
        return redirect('SurveyApp.views.survey_detail')
