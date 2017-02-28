# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.CharField(max_length=50)),
                ('wind', models.PositiveSmallIntegerField(default=0)),
                ('rain', models.PositiveSmallIntegerField(default=0)),
                ('snow', models.PositiveSmallIntegerField(default=0)),
                ('lightning', models.PositiveSmallIntegerField(default=0)),
                ('clouds', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('biome', models.PositiveSmallIntegerField(default=0)),
                ('day', models.PositiveIntegerField(default=900000)),
                ('night', models.PositiveIntegerField(default=900000)),
            ],
        ),
        migrations.CreateModel(
            name='ZoneState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tod', models.IntegerField(default=900000)),
                ('weather', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zone.Weather')),
            ],
        ),
        migrations.AddField(
            model_name='zone',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zone.ZoneState'),
        ),
    ]
