# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavioralactivation', '0002_auto_20150703_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sleeping', models.IntegerField(default=0)),
                ('mastery', models.IntegerField(default=0)),
                ('pleasure', models.IntegerField(default=0)),
                ('rumination', models.IntegerField(default=0)),
                ('distractionAndAvoidance', models.IntegerField(default=0)),
                ('miscellaneous', models.IntegerField(default=0)),
                ('week', models.IntegerField(default=0, unique=True)),
                ('user', models.ForeignKey(to='behavioralactivation.User')),
            ],
        ),
    ]
