# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problemset', '0001_initial'),
        ('submissions', '0011_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='problem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='problemset.Problem'),
            preserve_default=False,
        ),
    ]
