# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-16 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='description',
            field=models.TextField(verbose_name='权限描述'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=16, unique=True, verbose_name='权限名称'),
        ),
    ]