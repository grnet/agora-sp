# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0023_auto_20180615_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetails',
            name='visible_to_marketplace',
            field=models.BooleanField(default=False),
        ),
    ]
