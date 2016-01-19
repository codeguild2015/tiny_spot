# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0002_auto_20151228_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.FileField(upload_to='/static/img/%Y/%m/%d')),
            ],
        ),
    ]
