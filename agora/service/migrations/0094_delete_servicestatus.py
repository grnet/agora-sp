# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-07-20 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0093_auto_20200720_1333'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceStatus',
        ),
    ]
