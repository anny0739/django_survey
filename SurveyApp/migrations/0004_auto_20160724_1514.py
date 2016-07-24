# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SurveyApp', '0003_auto_20160724_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('response', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='surveyinfo',
            name='survey_id',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='etc',
            new_name='ans_content',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='contents',
            new_name='que_content',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='surveyInfo_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='survey_id',
        ),
        migrations.AddField(
            model_name='question',
            name='limit',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey_id',
            field=models.ForeignKey(to='SurveyApp.Survey', default='0'),
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(max_length=15, default='select'),
        ),
        migrations.AddField(
            model_name='user',
            name='question_id',
            field=models.ForeignKey(to='SurveyApp.Question', default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, default='0'),
        ),
        migrations.DeleteModel(
            name='SurveyInfo',
        ),
        migrations.AddField(
            model_name='entry',
            name='answer_id',
            field=models.ForeignKey(to='SurveyApp.Answer'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user_id',
            field=models.ForeignKey(to='SurveyApp.User'),
        ),
    ]
