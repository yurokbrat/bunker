# Generated by Django 5.0.9 on 2024-10-16 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalinfo',
            options={'verbose_name': 'доп. информация', 'verbose_name_plural': 'доп. информация'},
        ),
        migrations.AlterModelOptions(
            name='baggage',
            options={'verbose_name': 'багаж', 'verbose_name_plural': 'багажи'},
        ),
        migrations.AlterModelOptions(
            name='hobby',
            options={'verbose_name': 'хобби', 'verbose_name_plural': 'хобби'},
        ),
    ]
