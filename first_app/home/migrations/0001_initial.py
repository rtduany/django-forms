# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
				('email', models.EmailField()),
                ('interests', models.TextField()),
                ('registered_date', models.DateField(auto_now=False, auto_now_add=True)),
                ('last_update', models.DateField(auto_now_add=True, blank=False)),
            ],
        ),
    ]
