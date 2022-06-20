# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from accounts.models import Organisation
import json

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0057_auto_20220607_0727'),
    ]

    def migrate_string_to_json(apps, schema):
        for sample in Organisation.objects.all():
            try:
                if sample.epp_mri_multimedia!=None:
                    sample.epp_mri_multimedia = '{"multimedia link": "' + sample.epp_mri_multimedia + '"}'
                    sample.save()
            except:
                print('Cannot convert {} object'.format(sample.pk))

    operations = [
        migrations.RunPython(
            migrate_string_to_json
        ),
    ]
