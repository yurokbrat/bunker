from factory import SubFactory
from factory.django import DjangoModelFactory

from bunker_game.game.models.vote import Voting
from bunker_game.game.tests.factories.game_factory import GameFactory


class VotingFactory(DjangoModelFactory):
    game = SubFactory(GameFactory)

    class Meta:
        model = Voting
