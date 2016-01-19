# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tiny_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0005_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=200)),
                ('image', models.ImageField(verbose_name='Image', upload_to=tiny_app.models.upload_to)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'ordering': ('image',),
            },
        ),
        migrations.DeleteModel(
            name='Example',
        ),
    ]
