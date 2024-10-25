from bunker_game.game.models import Bunker, BunkerRoom, Catastrophe
from bunker_game.utils.get_random import random


def generate_random_bunker() -> Bunker:
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


def generate_random_catastrophe() -> Catastrophe:
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
