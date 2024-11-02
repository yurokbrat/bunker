from typing import Any

from factory import Faker, post_generation
from factory.django import DjangoModelFactory, ImageField

from bunker_game.game.models import Bunker
from bunker_game.game.tests.factories.bunker_factories.bunker_room_factory import (
    BunkerRoomFactory,
)


class BunkerFactory(DjangoModelFactory):
    name = Faker("text", locale="ru", max_nb_chars=120)
    description = Faker("text", locale="ru", max_nb_chars=120)
    image = ImageField()

    class Meta:
        model = Bunker

    @post_generation
    def bunker_rooms(self: Bunker, create: bool, *args: Any, **kwargs: Any) -> None:
        if create:
            bunker_rooms = BunkerRoomFactory.create_batch(size=3)
            self.rooms.set(bunker_rooms)
            self.save()
