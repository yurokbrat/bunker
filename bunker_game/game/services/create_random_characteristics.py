from typing import Any

from django.apps import apps
from django.db.models import Model

from bunker_game.game.enums import (
    ExperienceChoice,
    GenderChoice,
    OrientationChoice,
    PhobiaStageChoice,
    StatusBaggageChoice,
)
from bunker_game.game.models import (
    ActionCard,
    ActionCardUsage,
    AdditionalInfo,
    Character,
    Personage,
)
from bunker_game.utils.exceptions import NoDefaultCharacteristicError
from bunker_game.utils.get_random import random


def get_random_characteristic() -> dict[str, Any]:
    return {
        "age": random.randint(15, 60),
        "gender": random.choice(GenderChoice.values),
        "orientation": random.choice(OrientationChoice.values),
        "disease": create_random_characteristic(
            "Disease",
            {
                "degree_percent": random.randint(10, 100),
                "is_curable": random.choice([True, False]),
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


def create_random_characteristic(
    model_type: str,
    random_fields: dict[str, Any],
) -> Model:
    model = apps.get_model("game", model_type)
    default_characteristic = (
        model.objects.filter(is_generated=False).order_by("?").first()
    )
    if default_characteristic is None:
        raise NoDefaultCharacteristicError
    random_characteristic = model.objects.create(
        name=default_characteristic.name,
        is_generated=True,
    )

    if model_type == "Profession":
        random_characteristic.additional_skill = default_characteristic.additional_skill

    for field, value in random_fields.items():
        if hasattr(random_characteristic, field):
            setattr(random_characteristic, field, value)

    random_characteristic.save()
    return random_characteristic


def generate_random_action_cards(personage: Personage, count_cards: int = 3) -> None:
    random_cards = ActionCard.objects.order_by("?")[:count_cards]

    for card in random_cards:
        ActionCardUsage.objects.create(
            card=card,
            personage=personage,
            game=personage.game,
        )
