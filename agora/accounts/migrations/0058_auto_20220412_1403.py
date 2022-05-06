# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-12 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0057_organisation_epp_mri_multimedia_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, default=None, null=True)),
                ('url', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='epp_mri_multimedia_name',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='epp_mri_multimedia',
        ),
        migrations.AddField(
            model_name='organisation',
            name='epp_mri_multimedia',
            field=models.ManyToManyField(blank=True, related_name='multimedia', to='accounts.Multimedia'),
        ),
    ]
