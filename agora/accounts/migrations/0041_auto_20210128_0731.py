# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2021-01-28 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20201209_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]