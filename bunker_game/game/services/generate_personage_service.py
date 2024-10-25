import logging

from django.db import IntegrityError

from bunker_game.game.models import (
    Personage,
)
from bunker_game.game.services.create_random_characteristics import (
    generate_random_action_cards,
    get_random_characteristic,
)


class GeneratePersonageService:
    def __call__(self, personage: Personage) -> tuple[Personage, bool]:
        personage_data = get_random_characteristic()
        personage, created = Personage.objects.update_or_create(
            id=personage.id,
            defaults=personage_data,
        )
        if personage.action_cards.count() == 0:
            success = False
            while not success:
                try:
                    generate_random_action_cards(personage)
                    success = True
                except IntegrityError:
                    logging.warning(
                        "Не удалось сгенерировать уникальную карту. Повторяю попытку",
                    )

        return personage, created
