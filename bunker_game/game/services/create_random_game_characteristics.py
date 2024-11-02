from bunker_game.game.models import Bunker, BunkerRoom, Catastrophe
from bunker_game.utils.exceptions import NoDefaultCharacteristicError
from bunker_game.utils.get_random import random


def generate_random_bunker() -> Bunker:
    default_bunker = Bunker.objects.filter(is_generated=False).order_by("?").first()
    if default_bunker is None:
        raise NoDefaultCharacteristicError
    generated_bunker = Bunker.objects.create(
        name=default_bunker.name,
        description=default_bunker.description,
        image=default_bunker.image,
        is_generated=True,
    )
    bunker_rooms = BunkerRoom.objects.order_by("?")[:3]
    generated_bunker.rooms.set(bunker_rooms)
    return generated_bunker


def generate_random_catastrophe() -> Catastrophe:
    default_catastrophe = (
        Catastrophe.objects.filter(is_generated=False).order_by("?").first()
    )
    if default_catastrophe is None:
        raise NoDefaultCharacteristicError
    return Catastrophe.objects.create(
        name=default_catastrophe.name,
        description=default_catastrophe.description,
        image=default_catastrophe.image,
        is_generated=True,
        percent_population=random.randint(10, 80),
        impact_level=default_catastrophe.impact_level,
    )
