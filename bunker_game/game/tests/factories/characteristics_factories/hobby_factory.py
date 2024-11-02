from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import ExperienceChoice
from bunker_game.game.models import Hobby


class HobbyFactory(DjangoModelFactory):
    name = Faker("text", locale="ru", max_nb_chars=120)
    experience = FuzzyChoice(ExperienceChoice.values)

    class Meta:
        model = Hobby
