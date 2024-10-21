from bunker_game.game.models import Personage
from bunker_game.game.services.create_random_characteristic import (
    get_random_characteristic,
)


class RegenerateCharacteristicService:
    def __call__(self, personage: Personage, characteristic: str):
        old_value = getattr(personage, characteristic)
        new_value = self._get_new_value(characteristic)
        while old_value == new_value:
            new_value = self._get_new_value(characteristic)
        setattr(personage, characteristic, new_value)
        personage.save()
        return new_value

    def _get_new_value(self, characteristic: str):
        characteristic_map = get_random_characteristic()
        return characteristic_map[characteristic]
