# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='name',
            new_name='title',
        ),
    ]