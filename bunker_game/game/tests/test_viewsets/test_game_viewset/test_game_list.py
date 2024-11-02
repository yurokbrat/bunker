import pytest
from rest_framework import status

from bunker_game.game.tests.factories import GameFactory

pytestmark = pytest.mark.django_db


def test_game_list(user_api_client):
    games = GameFactory.create_batch(size=5)
    response = user_api_client.get("/api/games/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(games)
    assert response.data == [
        {
            "uuid": f"{game.uuid}",
            "creator": {
                "uuid": f"{game.creator.uuid}",
                "username": game.creator.username,
                "name": game.creator.name,
                "url": f"http://testserver{game.creator.get_absolute_url()}",
                "avatar": game.creator.avatar.url,
            },
            "personages_count": game.personages.count(),
            "personages": [
                {
                    "uuid": f"{personage.uuid}",
                    "user": {
                        "uuid": f"{personage.user.uuid}",
                        "username": personage.user.username,
                        "name": personage.user.name,
                        "url": f"http://testserver{personage.user.get_absolute_url()}",
                        "avatar": personage.user.avatar.url,
                    },
                    "age": personage.age,
                    "gender": personage.gender,
                    "orientation": personage.orientation,
                    "disease": {
                        "uuid": f"{personage.disease.uuid}",
                        "name": personage.disease.name,
                    },
                    "profession": {
                        "uuid": f"{personage.profession.uuid}",
                        "name": personage.profession.name,
                    },
                    "phobia": {
                        "uuid": f"{personage.phobia.uuid}",
                        "name": personage.phobia.name,
                    },
                    "hobby": {
                        "uuid": f"{personage.hobby.uuid}",
                        "name": personage.hobby.name,
                    },
                    "character": {
                        "uuid": f"{personage.character.uuid}",
                        "name": personage.character.name,
                    },
                    "additional_info": {
                        "uuid": f"{personage.additional_info.uuid}",
                        "name": personage.additional_info.name,
                    },
                    "baggage": {
                        "uuid": f"{personage.baggage.uuid}",
                        "name": personage.baggage.name,
                    },
                }
                for personage in game.personages.all()
            ],
            "bunker": {
                "uuid": f"{game.bunker.uuid}",
                "name": game.bunker.name,
                "image": game.bunker.image.url,
            },
            "catastrophe": {
                "uuid": f"{game.catastrophe.uuid}",
                "name": game.catastrophe.name,
                "image": game.catastrophe.image.url,
                "impact_level": game.catastrophe.impact_level,
            },
            "is_active": game.is_active,
        }
        for game in games
    ]
