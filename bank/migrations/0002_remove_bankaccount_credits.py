# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 02:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='credits',
        ),
    ]
