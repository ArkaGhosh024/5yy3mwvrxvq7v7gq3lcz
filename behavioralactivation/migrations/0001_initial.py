# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserSchedule',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('sleeping', models.IntegerField(default=0)),
                ('mastery', models.IntegerField(default=0)),
                ('pleasure', models.IntegerField(default=0)),
                ('rumination', models.IntegerField(default=0)),
                ('distractionAndAvoidance', models.IntegerField(default=0)),
                ('miscellaneous', models.IntegerField(default=0)),
                ('week', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to='behavioralactivation.User')),
            ],
        ),
    ]
