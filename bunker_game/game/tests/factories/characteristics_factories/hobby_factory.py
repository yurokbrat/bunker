from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import ExperienceChoice
from bunker_game.game.models import Hobby


class HobbyFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")
    experience = FuzzyChoice(ExperienceChoice.values)

    class Meta:
        model = Hobby
