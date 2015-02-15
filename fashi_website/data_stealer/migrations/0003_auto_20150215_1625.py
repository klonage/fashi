# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_stealer', '0002_auto_20150215_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='available_sizes',
            field=models.ManyToManyField(to='data_stealer.Size'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='price',
            name='value',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
