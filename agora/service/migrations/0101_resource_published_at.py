# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2021-01-28 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0100_auto_20210127_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
