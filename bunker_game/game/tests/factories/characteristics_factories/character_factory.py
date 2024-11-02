from factory import Faker
from factory.django import DjangoModelFactory

from bunker_game.game.models import Character


class CharacterFactory(DjangoModelFactory):
    name = Faker("text", locale="ru", max_nb_chars=120)

    class Meta:
        model = Character
