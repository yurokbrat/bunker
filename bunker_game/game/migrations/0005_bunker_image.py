# Generated by Django 5.0.9 on 2024-10-18 19:43

import bunker_game.utils.generate_hide_name
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_personage_age_alter_personage_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bunker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=bunker_game.utils.generate_hide_name.upload_to_bunkers, verbose_name='фотография'),
        ),
    ]