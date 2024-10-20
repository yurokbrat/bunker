# Generated by Django 5.0.9 on 2024-10-18 12:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_additionalinfo_options_alter_baggage_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacteristicVisibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic_type', models.CharField(choices=[('age', 'Возраст'), ('gender', 'Пол'), ('orientation', 'Ориентация'), ('disease', 'Здоровье'), ('profession', 'Профессия'), ('phobia', 'Фобия'), ('hobby', 'Хобби'), ('character', 'Характер'), ('additional_info', 'Доп. Информация'), ('baggage', 'Багаж')], max_length=30, verbose_name='тип характеристики')),
                ('is_hidden', models.BooleanField(default=True, verbose_name='скрыта')),
                ('personage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visibility', to='game.personage', verbose_name='персонаж')),
            ],
            options={
                'unique_together': {('personage', 'characteristic_type')},
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(auto_created=True, blank=True, null=True, verbose_name='игра создана в ')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='игра закончена в')),
                ('is_active', models.BooleanField(default=False, verbose_name='активна')),
                ('bunker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.bunker', verbose_name='бункер')),
                ('catastrophe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.catastrophe', verbose_name='катастрофа')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель игры')),
                ('personages', models.ManyToManyField(blank=True, related_name='games', to='game.personage', verbose_name='персонажи в игре')),
            ],
            options={
                'verbose_name': 'игра',
                'verbose_name_plural': 'игры',
            },
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.AddField(
            model_name='personage',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personages_in_game', to='game.game', verbose_name='игра'),
        ),
    ]
