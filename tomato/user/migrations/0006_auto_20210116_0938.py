# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-16 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210114_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Vip_end',
            new_name='vip_end',
        ),
    ]
