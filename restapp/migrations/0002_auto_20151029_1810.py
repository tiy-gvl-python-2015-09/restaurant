# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cuisine',
            field=models.IntegerField(null=True, choices=[(0, ''), (1, 'American'), (2, 'Italian'), (3, 'Japanese'), (4, 'Other')]),
        ),
    ]
