# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meatmarketrestservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemId',
            field=models.IntegerField(default=0),
        ),
    ]
