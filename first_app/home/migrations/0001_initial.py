# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('floor', models.CharField(max_length=20)),
                ('has_podium', models.CharField(max_length=20)),
                ('commissioned_date', models.DateTimeField(verbose_name=b'date commissioned')),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
