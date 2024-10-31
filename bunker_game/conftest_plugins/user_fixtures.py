import pytest

from bunker_game.users.models import User
from bunker_game.users.tests.factories import UserFactory


@pytest.fixture
def user(db) -> User:
    return UserFactory()
