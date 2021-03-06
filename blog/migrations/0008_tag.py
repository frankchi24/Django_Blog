# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-03 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170503_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=50, unique=True)),
                ('tag_slug', models.CharField(blank=True, max_length=50, unique=True)),
                ('posts', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]
