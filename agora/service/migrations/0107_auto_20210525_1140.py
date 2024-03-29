# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-25 11:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0106_auto_20210303_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resourceaudittable', to='service.Resource')),
                ('updater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='resourceaudit',
            unique_together=set([('resource', 'updated_at')]),
        ),
    ]
