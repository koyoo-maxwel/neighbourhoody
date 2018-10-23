# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0021_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='picture/'),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='loc',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kariobangi', 'Kariobangi'), ('Kilifi-Green Estate', 'Kilifi-Green Estate'), ('Kileleshwa', 'Kileleshwa'), ('Muhoroni', 'Muhoroni'), ('Kisumu', 'Kisumu'), ('Majengo', 'Majengo'), ('Mnarani', 'Mnarani'), ('Bofa', 'Bofa')], max_length=65),
        ),
    ]