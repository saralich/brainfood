# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seniorprojectapp', '0002_auto_20170412_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='active',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='afraid',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='alert',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='ashamed',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='attentive',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='determined',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='distressed',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='enthusiastic',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='excited',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='guilty',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='hostile',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='inspired',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='interested',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='irritable',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='jittery',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='nervous',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='proud',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='scared',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='strong',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='upset',
            field=models.CharField(choices=[('1', 'Very Slightly or Not At All'), ('2', 'A Little'), ('3', 'Moderately'), ('4', 'Quite a Bit'), ('5', 'Extremely')], max_length=1),
        ),
    ]
