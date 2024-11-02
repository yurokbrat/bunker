from rest_framework import status

from bunker_game.game.tests.factories import BunkerFactory, CatastropheFactory
from bunker_game.users.tests.factories import UserFactory


def test_new_game_start(user_api_client, new_game):
    default_bunker = BunkerFactory()
    default_catastrophe = CatastropheFactory()
    response = user_api_client.post(f"/api/games/{new_game.uuid}/start/")
    new_game.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "uuid": f"{new_game.uuid}",
        "creator": {
            "uuid": f"{new_game.creator.uuid}",
            "username": new_game.creator.username,
            "name": new_game.creator.name,
            "url": f"http://testserver{new_game.creator.get_absolute_url()}",
            "avatar": new_game.creator.avatar.url,
        },
        "personages_count": new_game.personages.count(),
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
                    "degree_percent": personage.disease.degree_percent,
                    "is_curable": personage.disease.is_curable,
                },
                "profession": {
                    "uuid": f"{personage.profession.uuid}",
                    "name": personage.profession.name,
                    "additional_skill": personage.profession.additional_skill,
                    "experience": f"{personage.profession.experience}",
                },
                "phobia": {
                    "uuid": f"{personage.phobia.uuid}",
                    "name": personage.phobia.name,
                    "stage": f"{personage.phobia.stage}",
                },
                "hobby": {
                    "uuid": f"{personage.hobby.uuid}",
                    "name": personage.hobby.name,
                    "experience": f"{personage.hobby.experience}",
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
                    "status": f"{personage.baggage.status}",
                },
                "action_cards": [
                    {
                        "uuid": f"{action_card_usage.uuid}",
                        "card": {
                            "uuid": f"{action_card_usage.card.uuid}",
                            "name": action_card_usage.card.name,
                            "key": action_card_usage.card.key,
                            "description": action_card_usage.card.description,
                            "target": action_card_usage.card.target,
                        },
                        "is_used": action_card_usage.is_used,
                    }
                    for action_card_usage in personage.action_cards.all()
                ],
            }
            for personage in new_game.personages.all()
        ],
        "bunker": {
            "uuid": f"{new_game.bunker.uuid}",
            "name": default_bunker.name,
            "description": default_bunker.description,
            "image": default_bunker.image.url,
            "rooms": [
                {
                    "uuid": f"{room.uuid}",
                    "name": room.name,
                    "area": room.area,
                }
                for room in new_game.bunker.rooms.all()
            ],
        },
        "catastrophe": {
            "uuid": f"{new_game.catastrophe.uuid}",
            "name": default_catastrophe.name,
            "description": default_catastrophe.description,
            "image": default_catastrophe.image.url,
            "percent_population": new_game.catastrophe.percent_population,
            "impact_level": default_catastrophe.impact_level,
        },
        "is_active": True,
        "num_places": new_game.num_places,
        "game_duration_type": new_game.game_duration_type,
        "time_in_bunker": new_game.time_in_bunker,
        "action_cards": [
            {
                "uuid": f"{action_card_usage.uuid}",
                "card": {
                    "uuid": f"{action_card_usage.card.uuid}",
                    "name": action_card_usage.card.name,
                    "key": action_card_usage.card.key,
                    "description": action_card_usage.card.description,
                    "target": action_card_usage.card.target,
                },
                "is_used": action_card_usage.is_used,
            }
            for action_card_usage in new_game.action_cards.all()
        ],
        "date_start": new_game.date_start.astimezone().isoformat(),
        "date_end": None,
    }


def test_active_game_start(creator_game_user_api_client, game):
    response = creator_game_user_api_client.post(f"/api/games/{game.uuid}/start/")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"detail": "Игра уже активна"}


def test_game_start_without_personages(user_api_client, new_game):
    BunkerFactory()
    CatastropheFactory()
    new_game.personages.clear()
    response = user_api_client.post(f"/api/games/{new_game.uuid}/start/")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"detail": "В игре нет персонажей"}


def test_game_start_no_creator(user_api_client, new_game):
    new_user = UserFactory()
    new_game.creator = new_user
    new_game.save()
    response = user_api_client.post(f"/api/games/{new_game.uuid}/start/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
