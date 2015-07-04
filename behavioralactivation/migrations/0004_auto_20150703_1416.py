# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavioralactivation', '0003_user_userschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userschedule',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserSchedule',
        ),
    ]
