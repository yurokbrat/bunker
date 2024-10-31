import pytest

from bunker_game.game.tests.factories import (
    ActionCardFactory,
    BunkerFactory,
    CatastropheFactory,
    GameFactory,
    PersonageFactory,
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
def personage():
    return PersonageFactory()
