import secrets
from typing import Any

from django.apps import apps
from django.db.models import Model

from bunker_game.game.constants import (
    ExperienceChoice,
    GenderChoice,
    OrientationChoice,
    PhobiaStageChoice,
    StatusBaggageChoice,
)
from bunker_game.game.models import AdditionalInfo, Character


def get_random_characteristic():
    return {
        "age": secrets.randbelow(71),
        "gender": secrets.choice(GenderChoice.values),
        "orientation": secrets.choice(OrientationChoice.values),
        "disease": create_random_characteristic(
            "Disease",
            {
                "degree_percent": secrets.randbelow(101),
                "is_curable": secrets.choice([True, False]),
            },
        ),
        "profession": create_random_characteristic(
            "Profession",
            {
                "experience": secrets.choice(ExperienceChoice.values),
            },
        ),
        "phobia": create_random_characteristic(
            "Phobia",
            {
                "stage": secrets.choice(PhobiaStageChoice.values),
            },
        ),
        "hobby": create_random_characteristic(
            "Hobby",
            {
                "experience": secrets.choice(ExperienceChoice.values),
            },
        ),
        "character": Character.objects.order_by("?").first(),
        "additional_info": AdditionalInfo.objects.order_by("?").first(),
        "baggage": create_random_characteristic(
            "Baggage",
            {
                "status": secrets.choice(StatusBaggageChoice.values),
            },
        ),
    }


def create_random_characteristic(model: str, random_fields: dict[str, Any]) -> Model:
    model = apps.get_model("game", model)
    characteristic_name = model.objects.order_by("?").first().name
    random_characteristic = model.objects.create(name=characteristic_name)

    for field, value in random_fields.items():
        if hasattr(random_characteristic, field):
            setattr(random_characteristic, field, value)

    random_characteristic.save()
    return random_characteristic
