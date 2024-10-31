from factory import SubFactory
from factory.django import DjangoModelFactory

from bunker_game.game.models import ActionCardUsage
from bunker_game.game.tests.factories.action_card_factory import ActionCardFactory
from bunker_game.game.tests.factories.game_factory import GameFactory
from bunker_game.game.tests.factories.personage_factory import PersonageFactory


class ActionCardUsageFactory(DjangoModelFactory):
    card = SubFactory(ActionCardFactory)
    personage = SubFactory(PersonageFactory)
    game = SubFactory(GameFactory)

    class Meta:
        model = ActionCardUsage
