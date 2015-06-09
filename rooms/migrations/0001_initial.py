# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_string', models.CharField(max_length=256)),
                ('repo', models.CharField(max_length=256)),
                ('clone_uri', models.CharField(max_length=256)),
            ],
        ),
    ]
