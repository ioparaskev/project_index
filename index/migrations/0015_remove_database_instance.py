# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20150903_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='database',
            name='instance',
        ),
    ]
