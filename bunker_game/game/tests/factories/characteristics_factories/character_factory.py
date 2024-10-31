from factory import Faker
from factory.django import DjangoModelFactory

from bunker_game.game.models import Character


class CharacterFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")

    class Meta:
        model = Character
