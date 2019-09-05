# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-05 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('shiptrader', '0003_listing_created')]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='cargo_capacity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='starship', name='crew', field=models.IntegerField(null=True)
        ),
        migrations.AlterField(
            model_name='starship',
            name='hyperdrive_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='starship', name='length', field=models.FloatField(null=True)
        ),
        migrations.AlterField(
            model_name='starship',
            name='passengers',
            field=models.IntegerField(null=True),
        ),
    ]
