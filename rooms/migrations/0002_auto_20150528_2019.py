# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_number', models.CharField(max_length=256)),
                ('room_type', models.CharField(max_length=256)),
                ('manager', models.CharField(max_length=256)),
                ('general_usage', models.BooleanField()),
                ('seating', models.IntegerField()),
                ('display', models.BooleanField()),
                ('phone', models.BooleanField()),
                ('network', models.BooleanField()),
                ('usage_restrictions', models.CharField(max_length=256)),
                ('has_usage_restrictions', models.BooleanField()),
                ('building', models.ForeignKey(to='rooms.Building')),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
