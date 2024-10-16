# Generated by Django 5.0.9 on 2024-10-16 14:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(auto_created=True, verbose_name='игра создана в ')),
                ('is_started', models.BooleanField(default=False, verbose_name='игра начата')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель комнаты')),
            ],
            options={
                'verbose_name': 'комната',
                'verbose_name_plural': 'комнаты',
            },
        ),
    ]
