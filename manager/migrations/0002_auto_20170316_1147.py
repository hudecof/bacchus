# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmbackups',
            name='size',
            field=models.BigIntegerField(default=0),
        ),
    ]
