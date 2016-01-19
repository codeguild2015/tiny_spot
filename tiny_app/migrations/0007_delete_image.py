# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0006_auto_20160113_1548'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
