# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-01 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='code',
        ),
        migrations.RemoveField(
            model_name='section',
            name='department',
        ),
        migrations.AddField(
            model_name='studyfield',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='section',
            name='studyfield',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.StudyField'),
            preserve_default=False,
        ),
    ]