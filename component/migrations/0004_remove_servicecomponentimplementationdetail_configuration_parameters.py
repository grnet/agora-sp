# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_servicedetailscomponent_configuration_parameters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecomponentimplementationdetail',
            name='configuration_parameters',
        ),
    ]
