# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-09 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0064_auto_20200509_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]