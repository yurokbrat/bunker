# Generated by Django 5.0.9 on 2024-10-21 09:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_user_last_online_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
