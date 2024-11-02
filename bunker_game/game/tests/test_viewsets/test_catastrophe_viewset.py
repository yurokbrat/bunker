import pytest
from rest_framework import status

from bunker_game.game.tests.factories import CatastropheFactory

pytestmark = pytest.mark.django_db


def test_catastrophe_list(user_api_client):
    catastrophes = CatastropheFactory.create_batch(5)
    response = user_api_client.get("/api/catastrophes/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(catastrophes)
    assert response.data == [
        {
            "uuid": f"{catastrophe.uuid}",
            "name": catastrophe.name,
            "image": catastrophe.image.url,
            "impact_level": catastrophe.impact_level,
        }
        for catastrophe in catastrophes
    ]


def test_catastrophe_detail(user_api_client, catastrophe):
    response = user_api_client.get(f"/api/catastrophes/{catastrophe.uuid}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "uuid": f"{catastrophe.uuid}",
        "name": catastrophe.name,
        "description": catastrophe.description,
        "image": catastrophe.image.url,
        "percent_population": catastrophe.percent_population,
        "impact_level": catastrophe.impact_level,
    }
