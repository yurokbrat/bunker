# Generated by Django 5.0.9 on 2024-10-22 15:42

import bunker_game.utils.generate_hide_name
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20241021_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='user-avatars/default.png', upload_to=bunker_game.utils.generate_hide_name.upload_to_avatars, verbose_name='аватар'),
        ),
    ]
