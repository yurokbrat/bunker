# Generated by Django 5.0.9 on 2024-10-21 09:11
import uuid

from django.db import migrations


def generate_uuid(apps, schema_editor):
    models_map = {
        "action_card": apps.get_model("game", "ActionCard"),
        "action_card_usage": apps.get_model("game", "ActionCardUsage"),
        "additional_info": apps.get_model("game", "AdditionalInfo"),
        "baggage": apps.get_model("game", "Baggage"),
        "bunker": apps.get_model("game", "Bunker"),
        "bunker_room": apps.get_model("game", "BunkerRoom"),
        "catastrophe": apps.get_model("game", "Catastrophe"),
        "character": apps.get_model("game", "Character"),
        "characteristic_visibility": apps.get_model("game", "CharacteristicVisibility"),
        "disease": apps.get_model("game", "Disease"),
        "game": apps.get_model("game", "Game"),
        "hobby": apps.get_model("game", "Hobby"),
        "personage": apps.get_model("game", "Personage"),
        "phobia": apps.get_model("game", "Phobia"),
        "profession": apps.get_model("game", "Profession"),
    }
    for model in models_map.values():
        for row in model.objects.iterator():
            row.uuid = uuid.uuid4()
            row.save(update_fields=["uuid"])


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0011_actioncard_uid_actioncardusage_uid_and_more'),
    ]

    operations = [
        migrations.RunPython(generate_uuid, reverse_code=migrations.RunPython.noop),
    ]