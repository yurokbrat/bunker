import pytest
from rest_framework import status

from bunker_game.game.enums import GameDurationType
from bunker_game.game.models import Game

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize("game_duration_type", GameDurationType.values)
def test_game_new(user_api_client, game_duration_type):
    response = user_api_client.post(
        "/api/games/new/",
        data={"game_duration_type": game_duration_type},
    )
    game = Game.objects.first()

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "uuid": f"{game.uuid}",
        "creator": {
            "uuid": f"{game.creator.uuid}",
            "username": game.creator.username,
            "name": game.creator.name,
            "url": f"http://testserver{game.creator.get_absolute_url()}",
            "avatar": game.creator.avatar.url,
        },
        "personages_count": 0,
        "personages": [],
        "bunker": None,
        "catastrophe": None,
        "is_active": False,
        "num_places": 0,
        "game_duration_type": game_duration_type,
        "time_in_bunker": "",
        "action_cards": [],
        "date_start": None,
        "date_end": None,
    }
    assert Game.objects.count() == 1
