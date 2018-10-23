# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0019_join'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='location',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
