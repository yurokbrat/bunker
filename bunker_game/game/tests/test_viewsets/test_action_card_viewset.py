import pytest
from rest_framework import status

from bunker_game.game.tests.factories import ActionCardFactory

pytestmark = pytest.mark.django_db


def test_action_card_list(user_api_client):
    action_cards = ActionCardFactory.create_batch(5)
    response = user_api_client.get("/api/action-cards/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(action_cards)
    assert response.data == [
        {
            "uuid": f"{action_card.uuid}",
            "name": action_card.name,
            "key": action_card.key,
        }
        for action_card in action_cards
    ]


def test_action_card_detail(user_api_client, action_card):
    response = user_api_client.get(f"/api/action-cards/{action_card.uuid}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "uuid": f"{action_card.uuid}",
        "name": action_card.name,
        "key": action_card.key,
        "description": action_card.description,
        "target": f"{action_card.target}",
    }
