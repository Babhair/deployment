# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20170201_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_hired',
        ),
    ]