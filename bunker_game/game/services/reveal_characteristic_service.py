from typing import Any

from django.db.models import Model
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from bunker_game.game.constants import DEFAULT_CHARACTERISTICS
from bunker_game.game.models import CharacteristicVisibility, Personage
from bunker_game.utils.format_characteristic_value import format_characteristic_value


class RevealCharacteristicService:
    def __call__(
        self,
        characteristic_type: str,
        personage: Personage,
        request: Request,
    ) -> Any:
        if characteristic_type not in DEFAULT_CHARACTERISTICS:
            error_message = "Invalid characteristic"
            raise ValidationError(error_message)
        visibility, _ = CharacteristicVisibility.objects.get_or_create(
            personage=personage,
            characteristic_type=characteristic_type,
        )
        visibility.is_hidden = False
        visibility.save()
        characteristic_value = getattr(personage, characteristic_type)
        if isinstance(characteristic_value, Model):
            characteristic_value = format_characteristic_value(
                characteristic_type,
                characteristic_value,
                request,
            ).data
        return characteristic_value
