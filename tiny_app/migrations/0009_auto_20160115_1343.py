# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0008_auto_20160115_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
