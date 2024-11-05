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
            generate_random_action_cards(personage)

        return personage, created
