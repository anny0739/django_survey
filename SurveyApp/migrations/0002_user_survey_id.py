# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SurveyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='survey_id',
            field=models.ForeignKey(to='SurveyApp.SurveyInfo', default='0'),
        ),
    ]
