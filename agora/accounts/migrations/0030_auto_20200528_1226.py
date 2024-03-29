# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-28 12:26
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20200512_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='pd_bai_0_id',
            field=models.TextField(blank=True, default=None, max_length=100, null=True, verbose_name=b'PD.BAI.0_ID'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_bai_1_name',
            field=models.CharField(default=None, max_length=100, null=True, unique=True, verbose_name=b'PD.BAI.1_Name'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_bai_2_abbreviation',
            field=models.CharField(default=None, max_length=30, null=True, verbose_name=b'PD.BAI.2_Abbreviation'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_cli_3_tags',
            field=models.TextField(blank=True, default=None, null=True, verbose_name=b'PD.CLI.3 Tags'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_2_postal_code',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name=b'PD.LOI.2 Postal Code'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_3_city',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name=b'PD.LOI.3 City'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_4_region',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name=b'PD.LOI.4 Region'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_5_country_or_territory',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name=b'PD.LOI.5 Country or Territory'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_mri_1_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=1000, null=True, verbose_name=b'PD.MRI.1_Description'),
        ),
    ]
