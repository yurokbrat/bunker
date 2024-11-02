from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import ActionCardTargetChoice
from bunker_game.game.models import ActionCard


class ActionCardFactory(DjangoModelFactory):
    name = Faker("text", locale="ru", max_nb_chars=120)
    key = Faker("text", locale="en_US", max_nb_chars=50)
    description = Faker("text", max_nb_chars=120)
    target = FuzzyChoice(ActionCardTargetChoice.values)

    class Meta:
        model = ActionCard
