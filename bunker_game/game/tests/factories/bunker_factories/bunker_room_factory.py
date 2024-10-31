from factory import Faker
from factory.django import DjangoModelFactory

from bunker_game.game.models import BunkerRoom


class BunkerRoomFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")
    area = Faker("pyint", min_value=1)

    class Meta:
        model = BunkerRoom
