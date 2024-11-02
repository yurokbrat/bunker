import pytest
from rest_framework import status

from bunker_game.game.tests.factories import BunkerFactory

pytestmark = pytest.mark.django_db


def test_bunker_list(user_api_client):
    bunkers = BunkerFactory.create_batch(5)
    response = user_api_client.get("/api/bunkers/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(bunkers)
    assert response.data == [
        {
            "uuid": f"{bunker.uuid}",
            "name": bunker.name,
            "image": bunker.image.url,
        }
        for bunker in bunkers
    ]


def test_bunker_detail(user_api_client, bunker):
    response = user_api_client.get(f"/api/bunkers/{bunker.uuid}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "uuid": f"{bunker.uuid}",
        "name": bunker.name,
        "description": bunker.description,
        "image": bunker.image.url,
        "rooms": [
            {
                "uuid": f"{room.uuid}",
                "name": room.name,
                "area": room.area,
            }
            for room in bunker.rooms.all()
        ],
    }
