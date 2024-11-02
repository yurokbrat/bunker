from rest_framework import status

from bunker_game.game.models import Personage


def test_new_game_connect(user_api_client, new_game):
    for personage in new_game.personages.all():
        personage.delete()
    new_game.save()
    response = user_api_client.post(f"/api/games/{new_game.uuid}/connect/")
    personage = Personage.objects.get(user=user_api_client.user)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "uuid": f"{new_game.uuid}",
        "creator": {
            "uuid": f"{new_game.creator.uuid}",
            "username": new_game.creator.username,
            "name": new_game.creator.name,
            "url": f"http://testserver{new_game.creator.get_absolute_url()}",
            "avatar": new_game.creator.avatar.url,
        },
        "personages_count": 1,
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
                "age": None,
                "gender": "",
                "orientation": "",
                "disease": None,
                "profession": None,
                "phobia": None,
                "hobby": None,
                "character": None,
                "additional_info": None,
                "baggage": None,
                "action_cards": [],
            },
        ],
        "bunker": None,
        "catastrophe": None,
        "is_active": False,
        "num_places": 0,
        "game_duration_type": new_game.game_duration_type,
        "time_in_bunker": "",
        "action_cards": [],
        "date_start": None,
        "date_end": None,
    }


def test_active_game_connect(user_api_client, game):
    response = user_api_client.post(f"/api/games/{game.uuid}/connect/")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"detail": "Игра уже активна"}
