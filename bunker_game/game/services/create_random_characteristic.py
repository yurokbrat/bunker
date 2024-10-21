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

random = secrets.SystemRandom()


def get_random_characteristic():
    return {
        "age": random.randint(15, 60),
        "gender": random.choice(GenderChoice.values),
        "orientation": random.choice(OrientationChoice.values),
        "disease": create_random_characteristic(
            "Disease",
            {
                "degree_percent": random.randint(10, 100),
                "is_curable": secrets.choice([True, False]),
            },
        ),
        "profession": create_random_characteristic(
            "Profession",
            {
                "experience": random.choice(ExperienceChoice.values),
            },
        ),
        "phobia": create_random_characteristic(
            "Phobia",
            {
                "stage": random.choice(PhobiaStageChoice.values),
            },
        ),
        "hobby": create_random_characteristic(
            "Hobby",
            {
                "experience": random.choice(ExperienceChoice.values),
            },
        ),
        "character": Character.objects.order_by("?").first(),
        "additional_info": AdditionalInfo.objects.order_by("?").first(),
        "baggage": create_random_characteristic(
            "Baggage",
            {
                "status": random.choice(StatusBaggageChoice.values),
            },
        ),
    }


def create_random_characteristic(model: str, random_fields: dict[str, Any]) -> Model:
    model = apps.get_model("game", model)
    characteristic_name = (
        model.objects.filter(is_generated=False).order_by("?").first().name
    )
    random_characteristic = model.objects.create(
        name=characteristic_name,
        is_generated=True,
    )

    for field, value in random_fields.items():
        if hasattr(random_characteristic, field):
            setattr(random_characteristic, field, value)

    random_characteristic.save()
    return random_characteristic
