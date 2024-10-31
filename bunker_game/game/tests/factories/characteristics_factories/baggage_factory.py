from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import StatusBaggageChoice
from bunker_game.game.models import Baggage


class BaggageFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")
    status = FuzzyChoice(StatusBaggageChoice.values)

    class Meta:
        model = Baggage
