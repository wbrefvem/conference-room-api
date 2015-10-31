# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20150528_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
