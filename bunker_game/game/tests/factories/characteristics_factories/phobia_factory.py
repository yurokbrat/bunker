from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import PhobiaStageChoice
from bunker_game.game.models import Phobia


class PhobiaFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")
    stage = FuzzyChoice(PhobiaStageChoice.values)

    class Meta:
        model = Phobia
