# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_auto_20170201_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
                ('users', models.ManyToManyField(related_name='trips_list', to='login.User')),
            ],
        ),
    ]