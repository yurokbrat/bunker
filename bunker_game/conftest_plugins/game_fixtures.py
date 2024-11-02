import pytest

from bunker_game.game.constants import DEFAULT_CHARACTERISTICS
from bunker_game.game.tests.factories import (
    ActionCardFactory,
    BunkerFactory,
    CatastropheFactory,
    GameFactory,
    PersonageFactory,
    VoteFactory,
    VotingFactory,
)


@pytest.fixture
def bunker():
    return BunkerFactory()


@pytest.fixture
def action_card():
    return ActionCardFactory()


@pytest.fixture
def catastrophe():
    return CatastropheFactory()


@pytest.fixture
def game():
    return GameFactory()


@pytest.fixture
def new_game(user):
    return GameFactory(
        creator=user,
        bunker=None,
        catastrophe=None,
        num_places=0,
        time_in_bunker="",
        is_active=False,
    )


@pytest.fixture
def personage():
    return PersonageFactory()


@pytest.fixture
def empty_personage(personage):
    for characteristic in DEFAULT_CHARACTERISTICS:
        if characteristic in frozenset(["gender", "orientation"]):
            setattr(personage, characteristic, "")
        else:
            setattr(personage, characteristic, None)
    personage.save()
    return personage


@pytest.fixture
def gaming_personage(game, personage):
    game.personages.add(personage)
    game.save()
    return personage


@pytest.fixture
def voting(game):
    return VotingFactory(game=game)


@pytest.fixture
def voting_with_votes(game, personage, voting):
    for game_personage in game.personages.all():
        VoteFactory(voting=voting, voter=game_personage, target=personage)
    return voting
