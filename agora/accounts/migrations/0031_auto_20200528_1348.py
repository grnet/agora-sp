# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-28 13:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20200528_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='pd_cli_1_scientific_domain',
            field=models.ManyToManyField(blank=True, related_name='domain_providers', to='accounts.Domain'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_cli_2_scientific_subdomain',
            field=models.ManyToManyField(blank=True, related_name='subdomain_providers', to='accounts.Subdomain'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_1_street_name_and_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_2_postal_code',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_3_city',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_4_region',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_loi_5_country_or_territory',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_mri_1_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_mri_2_logo',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_mri_3_multimedia',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_10_national_roadmaps',
            field=models.CharField(blank=True, default=None, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_3_affiliations',
            field=models.ManyToManyField(blank=True, related_name='affiliated_providers', to='accounts.Affiliation'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_4_networks',
            field=models.ManyToManyField(blank=True, related_name='networked_providers', to='accounts.Network'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_5_structure_type',
            field=models.ManyToManyField(blank=True, related_name='structured_providers', to='accounts.Structure'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_6_esfri_domain',
            field=models.ManyToManyField(blank=True, related_name='esfridomain_providers', to='accounts.EsfriDomain'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_7_esfri_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esfritype_providers', to='accounts.EsfriType'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_8_areas_of_activity',
            field=models.ManyToManyField(blank=True, related_name='activity_providers', to='accounts.Activity'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='pd_oth_9_societal_grand_challenges',
            field=models.ManyToManyField(blank=True, related_name='challenge_providers', to='accounts.Challenge'),
        ),
    ]
