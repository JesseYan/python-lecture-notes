# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160902_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='\u9996\u9875\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(default=False, verbose_name='\u5bfc\u822a\u663e\u793a'),
        ),
    ]
