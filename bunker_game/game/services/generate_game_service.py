from django.utils import timezone

from bunker_game.game.models import Catastrophe, Game
from bunker_game.game.services.generate_random_bunker import generate_random_bunker


class GenerateGameService:
    def __call__(self, game_id: int) -> Game:
        game_data = {
            "bunker": generate_random_bunker(),
            "catastrophe": Catastrophe.objects.order_by("?").first(),
            "date_start": timezone.now(),
            "is_active": True,
        }
        return Game.objects.filter(id=game_id).update(**game_data)
