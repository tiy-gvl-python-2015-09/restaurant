# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_order_submitted'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('count', models.IntegerField()),
                ('item', models.ForeignKey(to='restapp.Item')),
                ('order', models.ForeignKey(to='restapp.Order')),
            ],
        ),
    ]
