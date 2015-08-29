# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('ContactName', models.CharField(max_length=50)),
                ('TINNumber', models.CharField(max_length=50)),
                ('Address1', models.CharField(max_length=50)),
                ('Address2', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('ZIP', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AgencySupporterApproval',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Agency', models.ForeignKey(to='Next2U.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('ServiceName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Address1', models.CharField(max_length=50)),
                ('Address2', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('ZIP', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SupporterService',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Service', models.ForeignKey(to='Next2U.Service')),
                ('Supporter', models.ForeignKey(to='Next2U.Supporter')),
            ],
        ),
        migrations.AddField(
            model_name='agencysupporterapproval',
            name='Supporter',
            field=models.ForeignKey(to='Next2U.Supporter'),
        ),
    ]
