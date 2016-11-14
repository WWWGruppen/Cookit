# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-11 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161110_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookedRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_date', models.DateField(auto_now_add=True, verbose_name='Cooking Date')),
                ('cooking_time', models.TimeField(auto_now_add=True, verbose_name='Cooking Time')),
                ('serving_count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='history_recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='creation_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cookedrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Recipe'),
        ),
        migrations.AddField(
            model_name='cookedrecipe',
            name='user_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UserAccount'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='cooked_recipes',
            field=models.ManyToManyField(through='main.CookedRecipe', to='main.Recipe'),
        ),
    ]