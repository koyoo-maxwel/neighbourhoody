# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20181023_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hood_pic',
            new_name='picture',
        ),
    ]
