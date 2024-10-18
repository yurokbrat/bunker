import random

from bunker_game.game.models import (
    Personage,
    Disease,
    Profession,
    Phobia,
    Hobby,
    Character,
    AdditionalInfo,
    Baggage,
    personage,
)
from bunker_game.game.constants import GenderChoice, OrientationChoice
from bunker_game.users.models import User


class GeneratePersonageService:
    def __call__(self, user: User, game_id: id) -> Personage:
        personage_data = {
            "age": random.randint(10, 70),
            "gender": random.choice(GenderChoice.values),
            "orientation": random.choice(OrientationChoice.values),
            "disease": Disease.objects.order_by("?").first(),
            "profession": Profession.objects.order_by("?").first(),
            "phobia": Phobia.objects.order_by("?").first(),
            "hobby": Hobby.objects.order_by("?").first(),
            "character": Character.objects.order_by("?").first(),
            "additional_info": AdditionalInfo.objects.order_by("?").first(),
            "baggage": Baggage.objects.order_by("?").first(),
        }

        return Personage.objects.update_or_create(
            user=user, game_id=game_id, defaults=personage_data
        )
