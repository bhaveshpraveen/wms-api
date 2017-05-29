# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Readings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('temperature', models.IntegerField(default=0)),
                ('pressure', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
