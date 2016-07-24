# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SurveyApp', '0005_auto_20160724_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='ans_content',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='question',
            name='limit',
            field=models.IntegerField(default=0),
        ),
    ]
