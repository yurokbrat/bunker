import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_game_detail(user_api_client, game):
    personage = game.personages.first()
    personage.user = user_api_client.user
    personage.save()
    response = user_api_client.get(f"/api/games/{game.uuid}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
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
            for personage in game.personages.all()
        ],
        "bunker": {
            "uuid": f"{game.bunker.uuid}",
            "name": game.bunker.name,
            "description": game.bunker.description,
            "image": game.bunker.image.url,
            "rooms": [
                {
                    "uuid": f"{room.uuid}",
                    "name": room.name,
                    "area": room.area,
                }
                for room in game.bunker.rooms.all()
            ],
        },
        "catastrophe": {
            "uuid": f"{game.catastrophe.uuid}",
            "name": game.catastrophe.name,
            "description": game.catastrophe.description,
            "image": game.catastrophe.image.url,
            "percent_population": game.catastrophe.percent_population,
            "impact_level": game.catastrophe.impact_level,
        },
        "is_active": game.is_active,
        "num_places": game.num_places,
        "game_duration_type": game.game_duration_type,
        "time_in_bunker": game.time_in_bunker,
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
            for action_card_usage in game.action_cards.all()
        ],
        "date_start": game.date_start,
        "date_end": game.date_end,
    }
