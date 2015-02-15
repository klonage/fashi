# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_stealer', '0004_auto_20150215_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='size_type',
            field=models.IntegerField(choices=[(0, 'uni'), (1, 'pl-number')], default=0),
            preserve_default=False,
        ),
    ]
