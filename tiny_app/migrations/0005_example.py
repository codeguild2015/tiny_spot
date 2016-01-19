# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0004_delete_profileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('thumbnail', ajaximage.fields.AjaxImageField()),
            ],
        ),
    ]
