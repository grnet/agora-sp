# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0004_remove_servicecomponentimplementationdetail_configuration_parameters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedetailscomponent',
            name='configuration_parameters',
        ),
        migrations.AddField(
            model_name='servicecomponentimplementationdetail',
            name='configuration_parameters',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=None, null=True, blank=True),
        ),
    ]
