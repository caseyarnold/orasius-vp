# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0007_auto_20160805_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='forum_banned_lifted',
            field=models.DateTimeField(null=True),
        ),
    ]