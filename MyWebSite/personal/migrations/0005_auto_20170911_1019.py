# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 10:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20170911_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='title',
            new_name='name',
        ),
    ]
