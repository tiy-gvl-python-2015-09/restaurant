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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('fulfilled', models.BooleanField()),
                ('comments', models.TextField(blank=True)),
                ('items', models.ManyToManyField(to='restapp.Item')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone_num', models.CharField(blank=True, max_length=25)),
                ('cuisine', models.IntegerField(choices=[(0, ''), (1, 'American'), (2, 'Italian'), (3, 'Japanese'), (4, 'Other')])),
                ('allergies', models.TextField(blank=True)),
                ('user_type', models.CharField(max_length=20, choices=[('restaurant', 'Restaurant'), ('customer', 'Customer')], null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
