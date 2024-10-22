import random

from django.utils import timezone

from bunker_game.game.models import Bunker, BunkerRoom, Catastrophe, Game


class GenerateGameService:
    def __call__(self, game_id: int) -> Game:
        game_data = {
            "bunker": self._generate_random_bunker(),
            "catastrophe": self._generate_random_catastrophe(),
            "date_start": timezone.now(),
            "is_active": True,
        }
        return Game.objects.filter(id=game_id).update(**game_data)

    @staticmethod
    def _generate_random_bunker() -> Bunker:
        default_bunker = Bunker.objects.filter(is_generated=False).order_by("?").first()
        generated_bunker = Bunker.objects.create(
            name=default_bunker.name,
            description=default_bunker.description,
            image=default_bunker.image,
            is_generated=True,
        )
        bunker_rooms = BunkerRoom.objects.order_by("?")[:3]
        return generated_bunker.rooms.set(bunker_rooms)

    @staticmethod
    def _generate_random_catastrophe() -> Catastrophe:
        default_catastrophe = (
            Catastrophe.objects.filter(is_generated=False).order_by("?").first()
        )
        return Catastrophe.objects.create(
            name=default_catastrophe.name,
            description=default_catastrophe.description,
            image=default_catastrophe.image,
            is_generated=True,
            percent_population=random.randint(10, 80),
        )
