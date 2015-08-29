# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Next2U', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='Password',
            field=models.CharField(max_length=50, default='PWD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agency',
            name='Username',
            field=models.CharField(max_length=50, default='Helper'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supporter',
            name='Password',
            field=models.CharField(max_length=50, default='PWD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supporter',
            name='Username',
            field=models.CharField(max_length=50, default='Helper2'),
            preserve_default=False,
        ),
    ]
