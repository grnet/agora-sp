# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-18 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_auto_20210614_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='epp_loi_3_city',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
