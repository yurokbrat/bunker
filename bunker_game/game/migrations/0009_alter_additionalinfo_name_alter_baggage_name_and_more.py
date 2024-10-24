# Generated by Django 5.0.9 on 2024-10-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_remove_disease_degree_disease_degree_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='baggage',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=120, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='name',
            field=models.CharField(max_length=120, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='name',
            field=models.CharField(max_length=100, verbose_name='профессия'),
        ),
    ]
