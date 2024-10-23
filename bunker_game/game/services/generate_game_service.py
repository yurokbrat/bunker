from django.utils import timezone

from bunker_game.game.models import Bunker, BunkerRoom, Catastrophe, Game
from bunker_game.utils.get_random import random


class GenerateGameService:
    def __call__(self, game_id: int) -> Game:
        game_data = {
            "bunker": self._generate_random_bunker(),
            "catastrophe": self._generate_random_catastrophe(),
            "date_start": timezone.now(),
            "is_active": True,
        }
        Game.objects.filter(id=game_id).update(**game_data)
        return Game.objects.get(id=game_id)

    @staticmethod
    def _generate_random_bunker() -> Bunker:
        default_bunker = Bunker.objects.filter(is_generated=False).order_by("?").first()
        generated_bunker = Bunker.objects.create(
            name=default_bunker.name,  # type: ignore[union-attr]
            description=default_bunker.description,  # type: ignore[union-attr]
            image=default_bunker.image,  # type: ignore[union-attr]
            is_generated=True,
        )
        bunker_rooms = BunkerRoom.objects.order_by("?")[:3]
        generated_bunker.rooms.set(bunker_rooms)
        return generated_bunker

    @staticmethod
    def _generate_random_catastrophe() -> Catastrophe:
        default_catastrophe = (
            Catastrophe.objects.filter(is_generated=False).order_by("?").first()
        )
        return Catastrophe.objects.create(
            name=default_catastrophe.name,  # type: ignore[union-attr]
            description=default_catastrophe.description,  # type: ignore[union-attr]
            image=default_catastrophe.image,  # type: ignore[union-attr]
            is_generated=True,
            percent_population=random.randint(10, 80),
        )
