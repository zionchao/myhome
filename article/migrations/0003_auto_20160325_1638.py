# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160325_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
