# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-16 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_parser', '0005_parsedata_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='parsedata',
            name='experience',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
