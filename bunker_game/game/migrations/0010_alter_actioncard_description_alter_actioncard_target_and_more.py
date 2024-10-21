# Generated by Django 5.0.9 on 2024-10-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_alter_additionalinfo_name_alter_baggage_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actioncard',
            name='description',
            field=models.CharField(blank=True, max_length=120, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='actioncard',
            name='target',
            field=models.CharField(blank=True, choices=[('all', 'Все персонажи'), ('myself', 'На себя'), ('another_personage', 'Другой персонаж'), ('game', 'Игра')], max_length=30, verbose_name='цель'),
        ),
        migrations.AlterField(
            model_name='baggage',
            name='status',
            field=models.CharField(blank=True, choices=[('intact', 'Целый'), ('damaged', 'Поврежденный')], max_length=50, verbose_name='состояние'),
        ),
        migrations.AlterField(
            model_name='bunker',
            name='description',
            field=models.CharField(blank=True, max_length=120, verbose_name='описание бункера'),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='experience',
            field=models.CharField(blank=True, choices=[('novice', 'Новичок'), ('amateur', 'Любитель'), ('experienced', 'Опытный'), ('professional', 'Профессионал'), ('master', 'Мастер')], verbose_name='опыт хобби'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужчина'), ('female', 'Женщина')], verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='orientation',
            field=models.CharField(blank=True, choices=[('homosexual', 'Гомосексуален'), ('asexual', 'Асексуален'), ('heterosexual', 'Гетеросексуален')], verbose_name='ориентация'),
        ),
        migrations.AlterField(
            model_name='phobia',
            name='stage',
            field=models.CharField(blank=True, choices=[('none', 'Отсутствует'), ('mild', 'Легкая'), ('moderate', 'Средняя'), ('severe', 'Серьезная'), ('panic', 'Паническая')], max_length=120, verbose_name='стадия'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='experience',
            field=models.CharField(blank=True, choices=[('novice', 'Новичок'), ('amateur', 'Любитель'), ('experienced', 'Опытный'), ('professional', 'Профессионал'), ('master', 'Мастер')], verbose_name='опыт работы'),
        ),
    ]