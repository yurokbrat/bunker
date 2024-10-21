from bunker_game.game.models import (
    Personage,
)
from bunker_game.game.services.create_random_characteristic import (
    get_random_characteristic,
)


class GeneratePersonageService:
    def __call__(self, personage_id: int) -> Personage:
        personage_data = get_random_characteristic()
        return Personage.objects.update_or_create(
            id=personage_id,
            defaults=personage_data,
        )
