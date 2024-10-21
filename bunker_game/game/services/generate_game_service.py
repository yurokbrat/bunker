from django.utils import timezone

from bunker_game.game.models import Bunker, Catastrophe, Game


class GenerateGameService:
    def __call__(self, game_id: int) -> None:
        game_data = {
            "bunker": Bunker.objects.order_by("?").first(),
            "catastrophe": Catastrophe.objects.order_by("?").first(),
            "date_start": timezone.now(),
            "is_active": True,
        }
        Game.objects.filter(id=game_id).update(**game_data)
