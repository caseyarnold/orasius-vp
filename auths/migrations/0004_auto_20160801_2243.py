# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 02:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0003_auto_20160801_2235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]