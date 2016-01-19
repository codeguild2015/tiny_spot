# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tiny_app', '0007_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='/static/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.CharField(max_length=400)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(to='tiny_app.Post', default=None),
        ),
    ]
