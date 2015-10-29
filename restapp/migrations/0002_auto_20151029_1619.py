# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='type',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_num',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(max_length=20, null=True, choices=[('restaurant', 'Restaurant'), ('customer', 'Customer')]),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='allergies',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cuisine',
            field=models.IntegerField(null=True, choices=[(1, 'American'), (2, 'Italian'), (3, 'Japanese'), (4, 'Other')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
