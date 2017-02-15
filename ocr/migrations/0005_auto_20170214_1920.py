# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 23:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0004_auto_20170214_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programa',
            old_name='upload',
            new_name='pdf',
        ),
        migrations.AlterField(
            model_name='programa',
            name='creditos',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(16)]),
        ),
    ]