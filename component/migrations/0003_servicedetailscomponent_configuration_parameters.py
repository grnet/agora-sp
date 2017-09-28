# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0002_auto_20170731_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetailscomponent',
            name='configuration_parameters',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=None, null=True, blank=True),
        ),
    ]
