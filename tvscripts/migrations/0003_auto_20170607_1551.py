# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-07 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvscripts', '0002_auto_20170607_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='footnote',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='script',
            name='position',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]