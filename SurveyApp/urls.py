from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.survey_list, name='surveys'),
    #url(r'^surveys/([0-9]{4})/$', views.survey_detail),

]
