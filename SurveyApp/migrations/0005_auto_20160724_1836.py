# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SurveyApp', '0004_auto_20160724_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='que_content',
            new_name='title',
        ),
    ]
