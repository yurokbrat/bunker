from factory import SubFactory
from factory.django import DjangoModelFactory

from bunker_game.game.models.vote import Vote
from bunker_game.game.tests.factories.personage_factory import PersonageFactory
from bunker_game.game.tests.factories.voting_factories.voting_factory import (
    VotingFactory,
)


class VoteFactory(DjangoModelFactory):
    voting = SubFactory(VotingFactory)
    voter = SubFactory(PersonageFactory)
    target = SubFactory(PersonageFactory)

    class Meta:
        model = Vote
