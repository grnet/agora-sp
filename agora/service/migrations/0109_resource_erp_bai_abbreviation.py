# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-22 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0108_auto_20220322_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='erp_bai_abbreviation',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]