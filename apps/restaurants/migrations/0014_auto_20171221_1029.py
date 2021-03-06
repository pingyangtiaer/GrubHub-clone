# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_auto_20171220_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='menu_item',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.MenuItem'),
        ),
    ]
