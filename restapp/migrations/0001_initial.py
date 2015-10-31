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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('display', models.BooleanField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('count', models.IntegerField()),
                ('item', models.ForeignKey(to='restapp.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('fulfilled', models.BooleanField()),
                ('comments', models.TextField(blank=True)),
                ('submitted', models.BooleanField()),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='customer')),
                ('items', models.ManyToManyField(through='restapp.ItemCounter', to='restapp.Item')),
                ('restaurant', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
                ('phone_num', models.CharField(max_length=25, blank=True)),
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
