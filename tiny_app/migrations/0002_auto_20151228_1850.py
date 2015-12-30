# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='fullname',
        ),
        migrations.AddField(
            model_name='signup',
            name='full_name',
            field=models.CharField(null=True, max_length=120, blank=True),
        ),
    ]
