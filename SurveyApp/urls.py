from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.survey_list, name='surveys'),
    url(r'^survey/(?P<id>[0-9]+)/$', views.survey_detail),
    url(r'^survey/form/$', views.survey_form),

]
