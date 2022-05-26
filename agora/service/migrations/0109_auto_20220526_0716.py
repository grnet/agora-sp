# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-26 07:16
from __future__ import unicode_literals

from django.db import migrations, models
from service.models import Resource

class Migration(migrations.Migration):

    dependencies = [
        ('service', '0108_auto_20220526_0715'),
    ]
    
    def migrate_string_to_json(apps, schema):
        for sample in Resource.objects.all():
            try:
                if sample.erp_mri_4_multimedia!=None:
                    sample.erp_mri_4_multimedia = '{"multimedia link": "' + sample.erp_mri_4_multimedia + '"}'
                    sample.save()
            except:
                print('Cannot convert {} object'.format(sample.pk))


    operations = [
        migrations.AlterField(
            model_name='resource',
            name='erp_mri_4_multimedia',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.RunPython(
            migrate_string_to_json
        ),
    ]
