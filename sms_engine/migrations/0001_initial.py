# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'sent'), (1, 'failed')], verbose_name='Status')),
                ('exception_type', models.CharField(blank=True, max_length=255, verbose_name='Exception type')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=20, verbose_name='The destination number')),
                ('message', models.TextField(verbose_name='Content of sms')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'sent'), (1, 'failed'), (2, 'queued')], db_index=True, null=True, verbose_name='Status')),
                ('priority', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'low'), (1, 'medium'), (2, 'high'), (3, 'now')], null=True, verbose_name='Priority')),
                ('scheduled_time', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='The scheduled sending time')),
                ('backend_alias', models.CharField(blank=True, default=b'', max_length=64, verbose_name='Backend alias')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='sms',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='smses', to='sms_engine.SMS', verbose_name='SMS'),
        ),
    ]
