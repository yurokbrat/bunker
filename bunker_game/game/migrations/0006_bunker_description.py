# Generated by Django 5.0.9 on 2024-10-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_bunker_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bunker',
            name='description',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='описание бункера'),
        ),
    ]
