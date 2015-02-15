# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_stealer', '0006_auto_20150215_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size_type',
            field=models.IntegerField(choices=[(0, 'uni'), (1, 'pl-number')], blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='size',
            name='uni_value',
            field=models.IntegerField(choices=[(0, 'XS'), (1, 'S'), (3, 'L'), (2, 'M'), (3, 'L'), (4, 'XL'), (5, 'XXL')], blank=True, null=True),
            preserve_default=True,
        ),
    ]
