# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-05 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170506_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfeaturedimage',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
