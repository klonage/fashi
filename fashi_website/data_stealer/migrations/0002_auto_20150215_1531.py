# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_stealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compositor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('percentage_value', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompositorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('shop_url', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number_value', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UniSizes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='compositor',
            name='name',
            field=models.ForeignKey(to='data_stealer.CompositorType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clothes',
            name='compositors',
            field=models.ManyToManyField(to='data_stealer.Compositor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clothes',
            name='item_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clothes',
            name='picture_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clothes',
            name='shop',
            field=models.ForeignKey(default=1, to='data_stealer.Shop'),
            preserve_default=False,
        ),
    ]
