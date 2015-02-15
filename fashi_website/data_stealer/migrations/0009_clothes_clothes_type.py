# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_stealer', '0008_clothes_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='clothes_type',
            field=models.ForeignKey(to='data_stealer.ClothesType', default=1),
            preserve_default=False,
        ),
    ]
