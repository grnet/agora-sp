# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-06-10 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0080_auto_20200610_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='erp_mgi_3_user_manual',
            new_name='erp_mgi_2_user_manual',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='erp_mgi_4_terms_of_use',
            new_name='erp_mgi_3_terms_of_use',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='erp_mgi_5_privacy_policy',
            new_name='erp_mgi_4_privacy_policy',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='erp_mgi_2_helpdesk_email',
        ),
        migrations.AddField(
            model_name='resource',
            name='erp_mgi_5_access_policy',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
