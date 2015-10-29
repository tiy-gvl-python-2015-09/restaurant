# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('fulfilled', models.BooleanField()),
                ('comments', models.TextField()),
                ('items', models.ManyToManyField(to='restapp.Item')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('cuisine', models.CharField(max_length=15)),
                ('allergies', models.TextField()),
                ('type', models.CharField(max_length=1)),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
