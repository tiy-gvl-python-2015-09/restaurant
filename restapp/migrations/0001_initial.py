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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
                ('phone_num', models.CharField(max_length=25, blank=True)),
                ('cuisine', models.IntegerField(null=True, choices=[(1, 'American'), (2, 'Italian'), (3, 'Japanese'), (4, 'Other')])),
                ('allergies', models.TextField(blank=True)),
                ('user_type', models.CharField(max_length=20, null=True, choices=[('restaurant', 'Restaurant'), ('customer', 'Customer')])),
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
