# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCounter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('item', models.ForeignKey(to='restapp.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('fulfilled', models.BooleanField()),
                ('comments', models.TextField(blank=True)),
                ('submitted', models.BooleanField()),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='customer')),
                ('items', models.ManyToManyField(to='restapp.Item', through='restapp.ItemCounter')),
                ('restaurant', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone_num', models.CharField(blank=True, max_length=25)),
                ('cuisine', models.IntegerField(null=True, choices=[(1, 'American'), (2, 'Italian'), (3, 'Japanese'), (4, 'Other')])),
                ('allergies', models.TextField(blank=True)),
                ('user_type', models.CharField(max_length=20, null=True, choices=[('restaurant', 'Restaurant'), ('customer', 'Customer')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='itemcounter',
            name='order',
            field=models.ForeignKey(to='restapp.Order'),
        ),
    ]
