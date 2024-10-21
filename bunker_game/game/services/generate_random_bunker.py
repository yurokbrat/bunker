from bunker_game.game.models import Bunker, BunkerRoom


def generate_random_bunker() -> Bunker:
    default_bunker = Bunker.objects.filter(is_generated=False).order_by("?").first()
    generated_bunker = Bunker.objects.create(
        name=default_bunker.name,
        description=default_bunker.description,
        image=default_bunker.image,
        is_generated=True,
    )
    bunker_rooms = BunkerRoom.objects.order_by("?")[:3]
    generated_bunker.rooms.set(bunker_rooms)
    return generated_bunker
