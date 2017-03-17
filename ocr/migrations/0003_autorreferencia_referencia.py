# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_auto_20170315_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorreferencia',
            name='referencia',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ocr.ReferenciaBibliografica', verbose_name='referencia'),
            preserve_default=False,
        ),
    ]
