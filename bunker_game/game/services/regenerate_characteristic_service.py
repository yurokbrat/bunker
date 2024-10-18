import random

from bunker_game.game.constants import GenderChoice, OrientationChoice
from bunker_game.game.models import (
    Personage,
    Disease,
    Profession,
    Phobia,
    Hobby,
    Character,
    AdditionalInfo,
    Baggage,
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
        if characteristic == "age":
            return random.randint(10, 50)
        elif characteristic == "gender":
            return random.choice(GenderChoice.values)
        elif characteristic == "orientation":
            return random.choice(OrientationChoice.values)
        else:
            model_map = {
                "disease": Disease,
                "profession": Profession,
                "phobia": Phobia,
                "hobby": Hobby,
                "character": Character,
                "additional_info": AdditionalInfo,
                "baggage": Baggage,
            }
            return model_map[characteristic].objects.order_by("?").first()
