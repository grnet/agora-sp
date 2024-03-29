# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-28 09:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_auto_20220328_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_3_affiliations',
            new_name='epp_oth_affiliations',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_10_areas_of_activity',
            new_name='epp_oth_areas_of_activity',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_6_esfri_domain',
            new_name='epp_oth_esfri_domain',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_7_esfri_type',
            new_name='epp_oth_esfri_type',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_8_meril_scientific_domain',
            new_name='epp_oth_meril_scientific_domain',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_9_meril_scientific_subdomain',
            new_name='epp_oth_meril_scientific_subdomain',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_12_national_roadmaps',
            new_name='epp_oth_national_roadmaps',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_4_networks',
            new_name='epp_oth_networks',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_2_participating_countries',
            new_name='epp_oth_participating_countries',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_11_societal_grand_challenges',
            new_name='epp_oth_societal_grand_challenges',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='epp_oth_5_structure_type',
            new_name='epp_oth_structure_type',
        ),
    ]
