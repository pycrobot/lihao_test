# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-20 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fifaranking',
            name='rank_date',
            field=models.CharField(max_length=16),
        ),
    ]
