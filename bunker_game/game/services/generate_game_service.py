from django.utils import timezone

from bunker_game.game.models import Game
from bunker_game.game.services.create_random_game_characteristics import (
    generate_random_bunker,
    generate_random_catastrophe,
)
from bunker_game.utils.get_random import random


class GenerateGameService:
    def __call__(self, game: Game) -> Game:
        duration_map = {
            "short": random.randint(0, 2),
            "medium": random.randint(2, 4),
            "long": random.randint(4, 6),
        }
        places_diff = duration_map[game.game_duration_type]
        game_data = {
            "bunker": generate_random_bunker(),
            "catastrophe": generate_random_catastrophe(),
            "num_places": max(1, game.personages.count() - places_diff),
            "time_in_bunker": f"{random.randint(1, 20)} месяцев",
            "date_start": timezone.now(),
            "is_active": True,
        }
        Game.objects.filter(id=game.id).update(**game_data)
        game.refresh_from_db()
        return game
