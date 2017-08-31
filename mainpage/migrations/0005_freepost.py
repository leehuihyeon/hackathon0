# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-30 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_singsong'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createuser', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
