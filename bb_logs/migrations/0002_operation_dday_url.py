# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bb_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation_dday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Base')),
                ('operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Operation')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Base')),
            ],
        ),
    ]
