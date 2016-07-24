# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SurveyApp', '0002_user_survey_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('available_start_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('available_end_dt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='surveyinfo',
            name='available_end_dt',
        ),
        migrations.RemoveField(
            model_name='surveyinfo',
            name='available_start_dt',
        ),
        migrations.RemoveField(
            model_name='surveyinfo',
            name='title',
        ),
        migrations.AddField(
            model_name='surveyinfo',
            name='survey_id',
            field=models.ForeignKey(default='0', to='SurveyApp.Survey'),
        ),
    ]
