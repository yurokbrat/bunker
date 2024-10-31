from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import ExperienceChoice
from bunker_game.game.models import Profession


class ProfessionFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")
    experience = FuzzyChoice(ExperienceChoice.values)

    class Meta:
        model = Profession
