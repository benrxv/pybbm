# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pybb.util


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0002_auto_20141101_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='sort_order',
            field=models.PositiveIntegerField(default=1, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to=pybb.util.FilePathGenerator(to=b'pybb/avatar'), null=True, verbose_name='Avatar', blank=True),
        ),
    ]
