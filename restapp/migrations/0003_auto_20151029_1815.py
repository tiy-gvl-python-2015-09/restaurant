# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20151029_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cuisine',
            field=models.IntegerField(choices=[(0, ''), (1, 'American'), (2, 'Italian'), (3, 'Japanese'), (4, 'Other')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(max_length=20, blank=True, null=True, choices=[('restaurant', 'Restaurant'), ('customer', 'Customer')]),
        ),
    ]
