# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bb_logs', '0003_url_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bb_base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bb_operation_dday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('bb_base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Bb_base')),
            ],
        ),
        migrations.CreateModel(
            name='Bb_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bb_url', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('bb_base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Bb_base')),
            ],
        ),
        migrations.RenameModel(
            old_name='Operation',
            new_name='Bb_operation',
        ),
        migrations.RemoveField(
            model_name='base',
            name='operation',
        ),
        migrations.RemoveField(
            model_name='operation_dday',
            name='base',
        ),
        migrations.RemoveField(
            model_name='operation_dday',
            name='operation',
        ),
        migrations.RemoveField(
            model_name='url',
            name='base',
        ),
        migrations.RemoveField(
            model_name='url',
            name='operation',
        ),
        migrations.DeleteModel(
            name='Base',
        ),
        migrations.DeleteModel(
            name='Operation_dday',
        ),
        migrations.DeleteModel(
            name='Url',
        ),
        migrations.AddField(
            model_name='bb_url',
            name='bb_operation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Bb_operation'),
        ),
        migrations.AddField(
            model_name='bb_operation_dday',
            name='bb_operation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Bb_operation'),
        ),
        migrations.AddField(
            model_name='bb_base',
            name='bb_operation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb_logs.Bb_operation'),
        ),
    ]
