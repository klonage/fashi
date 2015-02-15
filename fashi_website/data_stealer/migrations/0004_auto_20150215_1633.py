# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_stealer', '0003_auto_20150215_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='uni_value',
            field=models.IntegerField(choices=[(0, 'XS'), (1, 'S'), (3, 'L'), (2, 'M'), (3, 'L'), (4, 'XL'), (5, 'XXL')], default=1),
            preserve_default=False,
        ),
    ]
