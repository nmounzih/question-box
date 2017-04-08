# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_box_app', '0002_auto_20170408_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='num_answers',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='num_views',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='num_answers',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='num_views',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]