# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_stealer', '0007_auto_20150215_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='colors',
            field=models.TextField(default='red'),
            preserve_default=False,
        ),
    ]
