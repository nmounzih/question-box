# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_box_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='num_answers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='num_views',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='num_answers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='num_views',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
