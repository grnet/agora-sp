# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-03 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_auto_20210303_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='eosc_updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='eosc_published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
