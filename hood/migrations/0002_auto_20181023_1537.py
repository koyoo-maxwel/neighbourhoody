# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='loc',
            new_name='location',
        ),
    ]
