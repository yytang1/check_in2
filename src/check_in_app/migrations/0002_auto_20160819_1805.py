# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_in_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='bankname',
            field=models.CharField(blank=True, db_column='bankname', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='banknum',
            field=models.CharField(blank=True, db_column='banknum', max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='hoteldays',
            field=models.IntegerField(blank=True, db_column='hoteldays', null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='pay',
            field=models.IntegerField(blank=True, db_column='pay', null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='phone',
            field=models.CharField(blank=True, db_column='phone', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='post',
            field=models.CharField(blank=True, db_column='post', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='room',
            field=models.CharField(blank=True, db_column='room', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='score',
            field=models.CharField(blank=True, db_column='score', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='ticketnum',
            field=models.CharField(blank=True, db_column='ticketnum', max_length=20, null=True),
        ),
    ]
