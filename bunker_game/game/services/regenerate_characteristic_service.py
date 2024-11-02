from typing import Any

from django.db.models import Model

from bunker_game.game.models import Personage
from bunker_game.game.services.create_random_characteristics import (
    get_random_characteristic,
)
from bunker_game.utils.exceptions import InvalidCharacteristicError


class RegenerateCharacteristicService:
    def __call__(self, personage: Personage, characteristic: str) -> int | Model | list:
        old_value = getattr(personage, characteristic)
        new_value = self._get_new_value(characteristic)
        while old_value == new_value:
            new_value = self._get_new_value(characteristic)
        setattr(personage, characteristic, new_value)
        personage.save()
        return new_value

    @staticmethod
    def _get_new_value(characteristic: str) -> Any:
        characteristic_map = get_random_characteristic()
        if characteristic_map.get(characteristic):
            return characteristic_map[characteristic]
        raise InvalidCharacteristicError
