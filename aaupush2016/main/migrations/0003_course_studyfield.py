# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-01 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160801_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='studyfield',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.StudyField'),
            preserve_default=False,
        ),
    ]